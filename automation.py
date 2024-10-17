from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Inflow:
    def __init__(self):
        # Set Chrome options
        chrome_options = Options()
        chrome_options.add_experimental_option(
            "detach", True
        )  # Keeps browser open after script ends

        self.driver = webdriver.Chrome(options=chrome_options)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org/")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(
            By.XPATH, '//*[@id="search-form"]/fieldset/button/i'
        )
        enter.click()
        p1 = self.driver.find_element(
            By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[1]'
        )
        return p1.text

    def player(self, query):
        # self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element(By.XPATH, '//*[@id="meta"]')
        video.click()
