from function_calling_usage import function_calling_usage
from grade_response_with_llm import grade_response_with_llm
from image_vision_usage import generate_image_vision_text

class ChatFlow:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages
    
    def chat(self, user_prompt):
        self.add_message({"role": "user", "content": user_prompt})
        response = function_calling_usage(user_prompt)
        self.add_message({"role": "assistant", "content": response})
        grade = self.grade_response(user_prompt, response)
        self.add_message({"role": "assistant", "content": f"Grade: {grade} \n\n this is the response: {response} that got this grade. adjust the response to improve the grade."})
        response = function_calling_usage(user_prompt)
        self.add_message({"role": "assistant", "content": response})
        return response
    
    def grade_response(self, user_prompt, assistant_response):
        grade = grade_response_with_llm(user_prompt, assistant_response)
        self.add_message({"role": "assistant", "content": grade})
        return grade

    def generate_image_vision_text(self, image_url):
        vision_text = generate_image_vision_text(image_url)
        self.add_message({"role": "assistant", "content": vision_text})
        return vision_text
# # # test the chat flow
# chat_flow = ChatFlow()
# print(chat_flow.chat("What are the latest models on huggingface? describe each of them to me in detail"))


