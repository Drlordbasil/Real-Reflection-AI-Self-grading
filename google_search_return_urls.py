import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import logging
from caching import cache

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def google_search(query, num_results=5, max_retries=3):
    cache_key = f"search_{query}_{num_results}"
    cached_result = cache.get(cache_key)
    if cached_result:
        logging.info(f"Returning cached result for query: {query}")
        return cached_result

    for attempt in range(max_retries):
        try:
            result = selenium_google_search(query, num_results, cache_key)
            if result:
                logging.info(f"Selenium search successful for query: {query}")
                return result
            else:
                logging.warning(f"Selenium search returned no results for query: {query}")
        except Exception as e:
            logging.warning(f"Selenium search failed (attempt {attempt + 1}/{max_retries}): {str(e)}. Retrying...")
            time.sleep(2 ** attempt)  # Exponential backoff

    logging.warning(f"All Selenium attempts failed. Falling back to requests method.")
    return requests_google_search(query, num_results, cache_key)

def selenium_google_search(query, num_results, cache_key):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        url = f"https://www.google.com/search?q={query}&num={num_results}"
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.g"))
        )

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return parse_google_results(soup, num_results, cache_key)

    finally:
        driver.quit()

def requests_google_search(query, num_results, cache_key):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    url = f"https://www.google.com/search?q={query}&num={num_results}"
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return parse_google_results(soup, num_results, cache_key)

def parse_google_results(soup, num_results, cache_key):
    search_results = []
    for result in soup.select('div.g'):
        title_element = result.select_one('h3')
        link_element = result.select_one('a')
        description_element = result.select_one('div.VwiC3b')
        
        if title_element and link_element and description_element:
            search_results.append({
                'title': title_element.text,
                'link': link_element['href'],
                'description': description_element.text.strip()
            })
        
        if len(search_results) >= num_results:
            break
    
    if not search_results:
        logging.warning("No search results found.")
        return json.dumps({"error": "No search results found"})
    
    result = json.dumps(search_results)
    cache.set(cache_key, result)
    return result

