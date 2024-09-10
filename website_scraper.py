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
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def scrape(self, url):
        cache_key = f"scrape_{url}"
        cached_result = cache.get(cache_key)
        if cached_result:
            logging.info(f"Returning cached result for URL: {url}")
            return cached_result

        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            text_content = soup.get_text(separator=' ', strip=True)
            
            cache.set(cache_key, text_content)
            return text_content
        except Exception as e:
            logging.error(f"Error scraping {url}: {str(e)}")
            return None

    def __del__(self):
        self.driver.quit()