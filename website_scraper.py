import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.parse import urlparse
import logging
from caching import cache

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class WebsiteScraper:
    last_request = {}

    @staticmethod
    def scrape_website(url, max_retries=3, backoff_factor=0.3):
        cache_key = f"scrape_{url}"
        cached_result = cache.get(cache_key)
        if cached_result:
            logging.info(f"Returning cached result for URL: {url}")
            return cached_result

        WebsiteScraper.rate_limit(url)

        for attempt in range(max_retries):
            try:
                result = WebsiteScraper.selenium_scrape(url, cache_key)
                logging.info(f"Selenium scraping successful for URL: {url}")
                return result
            except Exception as e:
                logging.warning(f"Selenium scraping failed (attempt {attempt + 1}/{max_retries}): {str(e)}. Retrying...")
                time.sleep(backoff_factor * (2 ** attempt))  # Exponential backoff

        logging.warning(f"All Selenium attempts failed. Falling back to requests method.")
        return WebsiteScraper.requests_scrape(url, cache_key)

    @staticmethod
    def selenium_scrape(url, cache_key):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            return WebsiteScraper.parse_content(driver.page_source, cache_key)
        finally:
            driver.quit()

    @staticmethod
    def requests_scrape(url, cache_key):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        return WebsiteScraper.parse_content(response.text, cache_key)

    @staticmethod
    def parse_content(html_content, cache_key):
        soup = BeautifulSoup(html_content, 'html.parser')

        for script in soup(["script", "style"]):
            script.decompose()

        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
        if main_content:
            text_content = main_content.get_text(separator='\n', strip=True)
        else:
            text_content = soup.get_text(separator='\n', strip=True)

        lines = (line.strip() for line in text_content.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text_content = '\n'.join(chunk for chunk in chunks if chunk)

        if not text_content:
            logging.warning("No content found on the page.")
            return "No content found on the page."

        max_length = 5000
        if len(text_content) > max_length:
            text_content = text_content[:max_length] + "..."

        cache.set(cache_key, text_content)
        return text_content

    @staticmethod
    def rate_limit(url):
        domain = urlparse(url).netloc
        if domain in WebsiteScraper.last_request:
            elapsed = time.time() - WebsiteScraper.last_request[domain]
            if elapsed < 5:
                wait_time = 5 - elapsed
                logging.info(f"Rate limiting for {domain}. Waiting {wait_time:.2f} seconds.")
                time.sleep(wait_time)
        WebsiteScraper.last_request[domain] = time.time()