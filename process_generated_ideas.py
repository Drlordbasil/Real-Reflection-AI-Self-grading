import os
import re
from collections import defaultdict
from chat_flow import ChatFlow

class IdeaProcessor:
    def __init__(self):
        self.chat_flow = ChatFlow()
        self.ideas = defaultdict(dict)

    def load_generated_ideas(self):
        folder = "generated_ideas"
        for filename in os.listdir(folder):
            if filename.endswith(".txt") and filename.startswith("idea_"):
                with open(os.path.join(folder, filename), "r", encoding="utf-8") as f:
                    content = f.read()
                    score = float(re.search(r"score_(\d+\.\d+)", filename).group(1))
                    self.ideas[score][filename] = content

    def extract_best_ideas(self, top_n=3):
        sorted_scores = sorted(self.ideas.keys(), reverse=True)
        return [list(self.ideas[score].values())[0] for score in sorted_scores[:top_n]]

    def combine_ideas(self, ideas):
        combined_prompt = "Combine and improve upon the following ideas to create a superior UBI solution:\n\n"
        for i, idea in enumerate(ideas, 1):
            combined_prompt += f"Idea {i}:\n{idea}\n\n"
        combined_prompt += "Provide a detailed description of the combined and improved idea."

        return self.chat_flow.chat(combined_prompt)

    def refine_prototype(self, idea):
        prompt = f"""
        Based on the following idea, create a more detailed and robust Python prototype:

        {idea}

        The prototype should:
        1. Include proper error handling and logging
        2. Follow best practices for code organization and modularity
        3. Implement key functionalities described in the idea
        4. Include comments explaining the code and its relation to the UBI solution
        5. Be runnable on any PC with standard Python libraries

        Provide the improved Python prototype as separate modules (e.g., main.py, utils.py, etc.) 
        with clear explanations for each module. Do not include any markdown formatting in the code.
        """
        return self.chat_flow.chat(prompt)

    def clean_code(self, code):
        # Remove markdown formatting
        code = re.sub(r'```python|```', '', code)
        # Remove any leading/trailing whitespace
        code = code.strip()
        return code

    def save_code_files(self, code):
        folder = "generated_ideas"
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Split the code into separate modules
        modules = re.split(r'\n{2,}(?=\w+\.py:)', code)

        for module in modules:
            match = re.match(r'(\w+\.py):(.*)', module, re.DOTALL)
            if match:
                filename, content = match.groups()
                content = self.clean_code(content)
                with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:
                    f.write(content)

    def process_ideas(self):
        print("Loading generated ideas...")
        self.load_generated_ideas()

        print("Extracting best ideas...")
        best_ideas = self.extract_best_ideas()

        print("Combining and improving ideas...")
        combined_idea = self.combine_ideas(best_ideas)

        print("Refining prototype...")
        refined_prototype = self.refine_prototype(combined_idea)

        print("Saving results...")
        with open("generated_ideas/combined_improved_idea.txt", "w", encoding="utf-8") as f:
            f.write(combined_idea)

        self.save_code_files(refined_prototype)

        print("Processing complete. Results saved in the generated_ideas folder.")

if __name__ == "__main__":
    processor = IdeaProcessor()
    processor.process_ideas()