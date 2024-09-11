import autogen
from autogen import UserProxyAgent, AssistantAgent, ConversableAgent
import os
from dotenv import load_dotenv

load_dotenv()

class AutogenCodeHandler:
    def __init__(self):
        self.config_list = [
            {
                "model": "llama-3.1-70b-versatile",
                "api_key": os.getenv("GROQ_API_KEY"),
                "base_url": "https://api.groq.com/openai/v1",
            }
        ]

        self.llm_config = {
            "config_list": self.config_list,
            "temperature": 0,
            "seed": 42,
        }

        self.user_proxy = UserProxyAgent(
            name="UserProxy",
            system_message="A human user who can execute Python code and provide feedback.",
            code_execution_config={"work_dir": "generated_ideas"},
            human_input_mode="NEVER",
            max_consecutive_auto_reply=1,
        )

        self.assistant = AssistantAgent(
            name="PythonExpert",
            system_message="You are a Python expert. Analyze, debug, and improve Python code.",
            llm_config=self.llm_config,
        )

    def _terminate_chat(self, sender: ConversableAgent, recipient: ConversableAgent):
        return True

    def _get_last_message(self, chat_history):
        if not chat_history:
            return "No response received from the assistant."
        return chat_history[-1]['content']

    def analyze_and_improve_code(self, code):
        self.user_proxy.initiate_chat(
            self.assistant,
            message=f"Analyze and improve the following Python code:\n\n{code}\n\nProvide suggestions for improvements, bug fixes, and optimizations.",
            termination_msg="TERMINATE",
            max_turns=3
        )
        
        chat_history = self.user_proxy.chat_messages[self.assistant.name]
        return self._get_last_message(chat_history)

    def test_code(self, code):
        self.user_proxy.initiate_chat(
            self.assistant,
            message=f"Test the following Python code and provide a summary of the results:\n\n{code}",
            termination_msg="TERMINATE",
            max_turns=3
        )
        
        chat_history = self.user_proxy.chat_messages[self.assistant.name]
        return self._get_last_message(chat_history)

    def debug_code(self, code, error_message):
        self.user_proxy.initiate_chat(
            self.assistant,
            message=f"Debug the following Python code that produced this error:\n\nCode:\n{code}\n\nError:\n{error_message}\n\nProvide a fix for the error.",
            termination_msg="TERMINATE",
            max_turns=3
        )
        
        chat_history = self.user_proxy.chat_messages[self.assistant.name]
        return self._get_last_message(chat_history)

# Example usage
if __name__ == "__main__":
    handler = AutogenCodeHandler()
    
    sample_code = """
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
    """
    
    analysis = handler.analyze_and_improve_code(sample_code)
    print("Code Analysis:")
    print(analysis)
    
    test_results = handler.test_code(sample_code)
    print("\nTest Results:")
    print(test_results)
    
    error_code = """
def divide_numbers(a, b):
    return a / b

result = divide_numbers(10, 0)
print(result)
    """
    
    debug_result = handler.debug_code(error_code, "ZeroDivisionError: division by zero")
    print("\nDebug Results:")
    print(debug_result)