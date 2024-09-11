import re
import os
from textblob import TextBlob
from chat_flow import ChatFlow

CONSTRAINTS = """
* Must be created in Python code and runnable on any PC.
* Must not use credentials ever or it can create its own credentials on its own autonomously.
* Must not cost anything to start at all.
* Can't rely on selling stuff that a person "already" has on hand.
* Can't rely on cash or trading stocks/crypto as that requires capital.
* Must be UBI (Universal Basic Income) temporary solutions for masses so it can't be saturated or able to be saturated.
"""

class IdeaGenerator:
    def __init__(self):
        self.chat_flow = ChatFlow()
        self.best_idea = None
        self.best_score = 0

    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity

    def extract_overall_score(self, evaluation):
        match = re.search(r"Overall score: (\d+(\.\d+)?)", evaluation)
        return float(match.group(1)) if match else 0

    def extract_improvement_suggestions(self, evaluation):
        match = re.search(r"Improvement suggestions:(.*?)(?=\n\n|\Z)", evaluation, re.DOTALL)
        return match.group(1).strip() if match else ""

    def generate_idea(self, is_refinement=False):
        if is_refinement:
            improvement_suggestions = self.extract_improvement_suggestions(
                self.chat_flow.chat(f"Evaluate the following idea:\n{self.best_idea}")
            )
            prompt = f"Refine this idea based on these suggestions:\n{self.best_idea}\n\nSuggestions:{improvement_suggestions}"
        else:
            prompt = f"""Generate an innovative idea for a Universal Basic Income (UBI) temporary solution that meets the following constraints:

            {CONSTRAINTS}

            The idea should leverage technology, particularly Python, to create a solution that can help people generate basic income without requiring initial capital or resources. Focus on digital solutions that can be easily distributed and scaled.
            """

        idea = self.chat_flow.chat(prompt)
        sentiment = self.analyze_sentiment(idea)
        evaluation = self.chat_flow.chat(f"Evaluate this idea:\n{idea}")
        overall_score = self.extract_overall_score(evaluation)

        return idea, sentiment, evaluation, overall_score

    def save_idea(self, idea, evaluation, score, sentiment, iteration):
        folder = "generated_ideas"
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        filename = f"{folder}/idea_{iteration:03d}_score_{score:.2f}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Idea:\n{idea}\n\nEvaluation:\n{evaluation}\n\nOverall Score: {score:.2f}\nSentiment: {sentiment:.2f}")

    def generate_python_prototype(self):
        prompt = f"Generate a Python prototype for this idea:\n{self.best_idea}"
        prototype = self.chat_flow.chat(prompt)
        
        with open("generated_ideas/best_idea_prototype.py", "w", encoding="utf-8") as f:
            f.write(prototype)
        
        return prototype

    def gen_idea_loop(self, max_iterations=20, refinement_threshold=7.5, excellent_idea_threshold=8.0):
        for iteration in range(1, max_iterations + 1):
            try:
                idea, sentiment, evaluation, overall_score = self.generate_idea(
                    is_refinement=(iteration > 1 and self.best_score >= refinement_threshold)
                )

                print(f"\n{'Refined' if iteration > 1 else 'Generated'} idea {iteration}:\n{idea}")
                print(f"Sentiment score: {sentiment:.2f}")
                print(f"Idea evaluation:\n{evaluation}")

                self.save_idea(idea, evaluation, overall_score, sentiment, iteration)

                if overall_score > self.best_score:
                    self.best_idea = idea
                    self.best_score = overall_score
                    print(f"New best idea! Score: {self.best_score:.2f}")

                if overall_score >= excellent_idea_threshold and sentiment > 0.5:
                    print(f"Excellent idea found after {iteration} iterations!")
                    break

            except Exception as e:
                print(f"Error occurred during iteration {iteration}: {e}")
                continue

        print(f"\nBest idea found after {iteration} iterations:")
        print(self.best_idea)
        print(f"Best idea score: {self.best_score:.2f}")

        try:
            print("\nGenerating Python prototype for the best idea...")
            prototype = self.generate_python_prototype()
            print("\nPython Prototype:")
            print(prototype)
        except Exception as e:
            print(f"Error generating or saving prototype: {e}")

if __name__ == "__main__":
    idea_generator = IdeaGenerator()
    idea_generator.gen_idea_loop()