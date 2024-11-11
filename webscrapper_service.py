from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape_terraform_documentation(url):
    # Set up the Chrome WebDriver
    service = Service("C:\\Windows\\System32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        # Open the webpage
        driver.get(url)

        # Wait for the content to load
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.ID, 'arguments-reference'))
        )

        # Get the page source and parse it with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find the <h2> tag with id 'arguments-reference'
        h2_tag = soup.find('h2', id='arguments-reference')

        if h2_tag:
            # Initialize an empty list to store <li> tags
            li_tags = []

            # Find the next sibling elements until the next <h2> tag
            sibling = h2_tag.find_next_sibling()
            while sibling and sibling.name != 'h2':
                if sibling.name == 'ul':
                    li_tags.extend(sibling.find_all('li'))
                sibling = sibling.find_next_sibling()

            # Return the text of each <li> tag
            return [tag.get_text() for tag in li_tags]
    finally:
        driver.quit()