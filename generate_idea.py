import re
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

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def evaluate_idea(chat_flow, idea):
    prompt = f"""Evaluate the following idea based on these criteria and constraints:

    Idea: {idea}

    Constraints:
    {CONSTRAINTS}

    Evaluate on a scale of 1-10 for each of these criteria:
    1. Novelty
    2. Feasibility
    3. Scalability
    4. Social impact
    5. Sustainability
    6. Accessibility
    7. Constraint compliance

    Provide your evaluation in the following format:
    Novelty: [score]
    Feasibility: [score]
    Scalability: [score]
    Social impact: [score]
    Sustainability: [score]
    Accessibility: [score]
    Constraint compliance: [score]
    
    Overall score: [weighted average of all scores, with constraint compliance weighted 3x]

    Strengths: [List 2-3 main strengths]
    Weaknesses: [List 2-3 main weaknesses]
    Improvement suggestions: [Provide 2-3 specific suggestions to improve the idea while maintaining constraint compliance]
    """
    
    evaluation = chat_flow.chat(prompt)
    return evaluation

def extract_overall_score(evaluation):
    match = re.search(r"Overall score: (\d+(\.\d+)?)", evaluation)
    if match:
        return float(match.group(1))
    return 0

def extract_improvement_suggestions(evaluation):
    match = re.search(r"Improvement suggestions:(.*?)(?=\n\n|\Z)", evaluation, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def refine_idea(chat_flow, idea, improvement_suggestions):
    prompt = f"""Refine the following idea based on these improvement suggestions while strictly adhering to the given constraints:

    Original idea: {idea}

    Improvement suggestions:
    {improvement_suggestions}

    Constraints:
    {CONSTRAINTS}

    Please provide an improved version of the idea that addresses these suggestions and fully complies with all constraints.
    """
    refined_idea = chat_flow.chat(prompt)
    return refined_idea

def generate_python_prototype(chat_flow, idea):
    prompt = f"""Create a simple Python prototype for the following idea:

    Idea: {idea}

    Requirements:
    1. The code should be runnable on any PC with Python installed.
    2. It should not require any external credentials or paid services.
    3. The prototype should demonstrate the core functionality of the idea.
    4. Include comments explaining the code and how it relates to the idea.
    5. Keep the code under 100 lines for simplicity.

    Please provide the Python code along with a brief explanation of how it works.
    """
    prototype = chat_flow.chat(prompt)
    return prototype

def gen_idea_loop():
    chat_flow = ChatFlow()
    ideas_generated = 0
    best_idea = None
    best_score = 0
    max_iterations = 20
    refinement_threshold = 7.5

    while ideas_generated < max_iterations:
        ideas_generated += 1
        
        if ideas_generated == 1 or best_score < refinement_threshold:
            prompt = f"""Generate an innovative idea for a Universal Basic Income (UBI) temporary solution that meets the following constraints:

            {CONSTRAINTS}

            The idea should leverage technology, particularly Python, to create a solution that can help people generate basic income without requiring initial capital or resources. Focus on digital solutions that can be easily distributed and scaled.
            """
            idea = chat_flow.chat(prompt)
            print(f"\nGenerated idea {ideas_generated}:\n{idea}")
        else:
            improvement_suggestions = extract_improvement_suggestions(evaluate_idea(chat_flow, best_idea))
            idea = refine_idea(chat_flow, best_idea, improvement_suggestions)
            print(f"\nRefined idea {ideas_generated}:\n{idea}")

        sentiment = analyze_sentiment(idea)
        print(f"Sentiment score: {sentiment:.2f}")

        evaluation = evaluate_idea(chat_flow, idea)
        print(f"Idea evaluation:\n{evaluation}")

        overall_score = extract_overall_score(evaluation)
        
        if overall_score > best_score:
            best_idea = idea
            best_score = overall_score
            print(f"New best idea! Score: {best_score:.2f}")

        if overall_score >= 8.5 and sentiment > 0.6:
            print(f"Excellent idea found after {ideas_generated} iterations!")
            break

    print(f"\nBest idea found after {ideas_generated} iterations:")
    print(best_idea)
    print(f"Best idea score: {best_score:.2f}")

    # Generate Python prototype for the best idea
    print("\nGenerating Python prototype for the best idea...")
    prototype = generate_python_prototype(chat_flow, best_idea)
    print("\nPython Prototype:")
    print(prototype)

if __name__ == "__main__":
    gen_idea_loop()