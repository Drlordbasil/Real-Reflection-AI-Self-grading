from load_client import load_client
from config import Config
from image_vision_usage import generate_image_vision_text
from google_search_return_urls import google_search
from website_scraper import WebsiteScraper
import json
import re
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

client = load_client()

def function_calling_usage(query):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages = [
        {"role": "system", "content": f"You are a helpful assistant that can search the internet for information, scrape websites, and analyze images. After gathering all necessary information, provide a comprehensive response to the user's query. The current date and time is {current_datetime}."},
        {"role": "user", "content": query}
    ]

    # Check for image URLs in the query
    image_urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', query)
    if image_urls:
        for url in image_urls:
            image_description = generate_image_vision_text(url)
            messages.append({"role": "system", "content": f"Image description: {image_description}"})

    # Load tools from JSON file
    with open("tools_functions.json", "r") as f:
        tools = json.load(f)

    while True:
        try:
            response = client.chat.completions.create(
                model=Config.regular_model,
                messages=messages,
                tools=tools,
                tool_choice="auto"
            )

            assistant_message = response.choices[0].message
            messages.append(assistant_message)

            if not assistant_message.tool_calls:
                # If no more tool calls, this is the final response
                return assistant_message.content

            for tool_call in assistant_message.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                logging.debug(f"Calling function: {function_name} with arguments: {arguments}")

                if function_name == "google_search":
                    try:
                        search_results = google_search(arguments["query"])
                        logging.debug(f"Google search results: {search_results[:100]}...")  # Log first 100 chars
                        messages.append({"role": "tool", "content": search_results, "tool_call_id": tool_call.id})
                    except Exception as e:
                        logging.error(f"Google search failed: {str(e)}")
                        messages.append({"role": "tool", "content": f"Google search failed: {str(e)}", "tool_call_id": tool_call.id})
                elif function_name == "scrape_website":
                    try:
                        scraped_content = WebsiteScraper.scrape_website(arguments["url"])
                        logging.debug(f"Scraped content: {scraped_content[:100]}...")  # Log first 100 chars
                        messages.append({"role": "tool", "content": scraped_content, "tool_call_id": tool_call.id})
                    except Exception as e:
                        logging.error(f"Website scraping failed for {arguments['url']}: {str(e)}")
                        messages.append({"role": "tool", "content": f"Website scraping failed: {str(e)}", "tool_call_id": tool_call.id})

        except Exception as e:
            logging.error(f"An error occurred during function calling: {str(e)}")
            return f"An error occurred while processing your request: {str(e)}"

    # This line should never be reached, but just in case:
    return "An error occurred while processing your request."

if __name__ == "__main__":
    result = function_calling_usage("What are the latest models on huggingface?")
    print(result)