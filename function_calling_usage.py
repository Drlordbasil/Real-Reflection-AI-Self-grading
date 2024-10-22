from load_client import load_client
from config import Config
from image_vision_usage import generate_image_vision_text
from google_search_return_urls import google_search
from website_scraper import WebsiteScraper
from autogen_code_handler import AutogenCodeHandler
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

client = load_client()
autogen_handler = AutogenCodeHandler()

def function_calling_usage(user_prompt):
    with open('tools_functions.json', 'r') as f:
        tools = json.load(f)

    try:
        response = client.chat.completions.create(
            model=Config.text_gen_funct_call_model,
            messages=[{"role": "user", "content": user_prompt}],
            tools=tools,
            tool_choice="auto"
        )

        if response.choices[0].message.tool_calls:
            for tool_call in response.choices[0].message.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                logging.info(f"Function called: {function_name}")
                logging.info(f"Function arguments: {function_args}")

                if function_name == "google_search":
                    search_results = google_search(function_args["query"])
                    return f"Search results for '{function_args['query']}': {search_results}"
                elif function_name == "scrape_website":
                    scraper = WebsiteScraper()
                    content = scraper.scrape(function_args["url"])
                    if content:
                        return f"Content from {function_args['url']}: {content}"
                    else:
                        return f"Failed to scrape content from {function_args['url']}"
                elif function_name == "analyze_and_improve_code":
                    analysis = autogen_handler.analyze_and_improve_code(function_args["code"])
                    return f"Code analysis and improvement suggestions:\n{analysis}"
                elif function_name == "test_code":
                    test_results = autogen_handler.test_code(function_args["code"])
                    return f"Code test results:\n{test_results}"
                elif function_name == "debug_code":
                    debug_result = autogen_handler.debug_code(function_args["code"], function_args["error_message"])
                    return f"Code debugging results:\n{debug_result}"
                else:
                    return f"Unknown function: {function_name}"
        else:
            return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error in function_calling_usage: {str(e)}")
        return f"An error occurred: {str(e)}"