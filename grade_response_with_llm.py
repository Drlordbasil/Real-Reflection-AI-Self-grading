from function_calling_usage import function_calling_usage

def grade_response_with_llm(user_prompt, assistant_response):
    # call function_calling_usage to get the response
    structured_grading_prompt = f"""
    You are a helpful assistant that can grade the response of a user.
    You will be given a response and will grade it based on the criteria provided.
    You will need to grade the response based on what you think the user is looking for.
    You will need to return a grade and a explanation for the grade.
    ### user prompt: {user_prompt}
    ### assistant response: {assistant_response}
    """
    # call function_calling_usage to get the response
    response = function_calling_usage(structured_grading_prompt)
    return response

# test this function
# user_prompt = "What is the capital of the moon?"
# assistant_response = "The capital of the moon is called New Moon City."
# print(grade_response_with_llm(user_prompt, assistant_response))
