from load_client import load_client
from config import Config
from image_vision_usage import generate_image_vision_text
from google_search_return_urls import google_search
from website_scraper import WebsiteScraper
import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

client = load_client()

def function_calling_usage(user_prompt):
    with open('tools_functions.json', 'r') as f:
        tools = json.load(f)

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

            if function_name == "google_search":
                search_results = google_search(function_args["query"])
                return f"Search results for '{function_args['query']}': {search_results}"
            elif function_name == "scrape_website":
                scraper = WebsiteScraper()
                content = scraper.scrape(function_args["url"])
                return f"Content from {function_args['url']}: {content}"
    else:
        return response.choices[0].message.content