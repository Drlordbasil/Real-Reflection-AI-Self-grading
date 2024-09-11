import numpy as np
from datasets import load_dataset
from transformers import AutoTokenizer
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer
from sklearn.metrics import accuracy_score
from chat_flow import ChatFlow
import nltk
import logging
import matplotlib.pyplot as plt
from datetime import datetime

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BenchmarkTesting:
    def __init__(self):
        self.chat_flow = ChatFlow()
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")  # Using GPT-2 tokenizer for consistency
        self.rouge_scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

    def preprocess_text(self, text):
        return ' '.join(self.tokenizer.tokenize(text))

    def calculate_bleu(self, reference, candidate):
        try:
            reference_tokens = nltk.word_tokenize(self.preprocess_text(reference))
            candidate_tokens = nltk.word_tokenize(self.preprocess_text(candidate))
            return sentence_bleu([reference_tokens], candidate_tokens)
        except LookupError as e:
            logging.error(f"NLTK resource error: {str(e)}")
            return 0

    def calculate_rouge(self, reference, candidate):
        scores = self.rouge_scorer.score(reference, candidate)
        return {key: value.fmeasure for key, value in scores.items()}

    def run_qa_benchmark(self, num_samples=100):
        dataset = load_dataset("squad", split="validation[:100]")
        bleu_scores = []
        rouge_scores = []

        for i, example in enumerate(dataset):
            if i >= num_samples:
                break

            context = example['context']
            question = example['question']
            reference_answer = example['answers']['text'][0]

            prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
            try:
                model_answer = self.chat_flow.chat(prompt)
                bleu_score = self.calculate_bleu(reference_answer, model_answer)
                rouge_score = self.calculate_rouge(reference_answer, model_answer)

                bleu_scores.append(bleu_score)
                rouge_scores.append(rouge_score)

                logging.info(f"Processed QA sample {i+1}/{num_samples}")
            except Exception as e:
                logging.error(f"Error processing QA sample {i+1}: {str(e)}")

        if bleu_scores and rouge_scores:
            avg_bleu = np.mean(bleu_scores)
            avg_rouge = {key: np.mean([score[key] for score in rouge_scores]) for key in rouge_scores[0]}
            return {"bleu": avg_bleu, "rouge": avg_rouge}
        else:
            logging.warning("No valid scores were calculated for QA benchmark")
            return {"bleu": 0, "rouge": {}}

    def run_summarization_benchmark(self, num_samples=100):
        dataset = load_dataset("cnn_dailymail", "3.0.0", split="validation[:100]")
        rouge_scores = []

        for i, example in enumerate(dataset):
            if i >= num_samples:
                break

            article = example['article']
            reference_summary = example['highlights']

            prompt = f"Summarize the following article:\n\n{article}\n\nSummary:"
            model_summary = self.chat_flow.chat(prompt)

            rouge_score = self.calculate_rouge(reference_summary, model_summary)
            rouge_scores.append(rouge_score)

            logging.info(f"Processed summarization sample {i+1}/{num_samples}")

        avg_rouge = {key: np.mean([score[key] for score in rouge_scores]) for key in rouge_scores[0]}
        return avg_rouge

    def run_sentiment_analysis_benchmark(self, num_samples=100):
        dataset = load_dataset("imdb", split="test[:100]")
        predictions = []
        true_labels = []

        for i, example in enumerate(dataset):
            if i >= num_samples:
                break

            text = example['text']
            true_label = example['label']

            prompt = f"Classify the sentiment of the following movie review as positive or negative:\n\n{text}\n\nSentiment:"
            model_sentiment = self.chat_flow.chat(prompt).strip().lower()

            predictions.append(1 if model_sentiment == "positive" else 0)
            true_labels.append(true_label)

            logging.info(f"Processed sentiment analysis sample {i+1}/{num_samples}")

        accuracy = accuracy_score(true_labels, predictions)
        return accuracy

    def run_all_benchmarks(self, num_samples=100):
        results = {}
        
        logging.info("Starting QA benchmark")
        results["qa"] = self.run_qa_benchmark(num_samples)
        
        logging.info("Starting summarization benchmark")
        results["summarization"] = self.run_summarization_benchmark(num_samples)
        
        logging.info("Starting sentiment analysis benchmark")
        results["sentiment_analysis"] = self.run_sentiment_analysis_benchmark(num_samples)

        return results

    def plot_results(self, results):
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))
        fig.suptitle('Benchmark Results', fontsize=16)

        # QA Benchmark
        qa_scores = [results['qa']['bleu']] + list(results['qa']['rouge'].values())
        qa_labels = ['BLEU'] + list(results['qa']['rouge'].keys())
        ax1.bar(qa_labels, qa_scores)
        ax1.set_title('Question Answering')
        ax1.set_ylim(0, 1)
        for i, v in enumerate(qa_scores):
            ax1.text(i, v, f'{v:.2f}', ha='center', va='bottom')

        # Summarization Benchmark
        summarization_scores = list(results['summarization'].values())
        summarization_labels = list(results['summarization'].keys())
        ax2.bar(summarization_labels, summarization_scores)
        ax2.set_title('Summarization')
        ax2.set_ylim(0, 1)
        for i, v in enumerate(summarization_scores):
            ax2.text(i, v, f'{v:.2f}', ha='center', va='bottom')

        # Sentiment Analysis Benchmark
        ax3.bar(['Accuracy'], [results['sentiment_analysis']])
        ax3.set_title('Sentiment Analysis')
        ax3.set_ylim(0, 1)
        ax3.text(0, results['sentiment_analysis'], f'{results["sentiment_analysis"]:.2f}', ha='center', va='bottom')

        plt.tight_layout()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'benchmark_results_{timestamp}.png'
        plt.savefig(filename)
        logging.info(f"Benchmark results saved as {filename}")
        plt.close()

if __name__ == "__main__":
    benchmark = BenchmarkTesting()
    results = benchmark.run_all_benchmarks(num_samples=10)  # Adjust the number of samples as needed
    
    print("\nBenchmark Results:")
    if "qa" in results:
        print("Question Answering:")
        print(f"BLEU Score: {results['qa'].get('bleu', 0):.4f}")
        print(f"ROUGE Scores: {results['qa'].get('rouge', {})}")
    
    if "summarization" in results:
        print("\nSummarization:")
        print(f"ROUGE Scores: {results['summarization']}")
    
    if "sentiment_analysis" in results:
        print("\nSentiment Analysis:")
        print(f"Accuracy: {results['sentiment_analysis']:.4f}")
    
    benchmark.plot_results(results)