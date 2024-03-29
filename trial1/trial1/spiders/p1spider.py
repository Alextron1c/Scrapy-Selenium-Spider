import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class p1spider(scrapy.Spider):
    name = "p1spider"
    allowed_domains = ["ccmspa.pinellascounty.org"]
    start_urls = ["https://ccmspa.pinellascounty.org/PublicAccess/default.aspx"]

    def __init__(self, input_1=None, input_2=None, *args, **kwargs):
        super(p1spider, self).__init__(*args, **kwargs)
        self.input_1 = input_1
        self.input_2 = input_2
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        
        probate_records_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Probate Case Records"))
        )        
        probate_records_link.click()

        radio_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "DateFiled"))
        )        
        radio_button.click()

        time.sleep(3)

        date_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "DateFiledOnAfter"))
        )
        date_field.clear()
        date_field.send_keys(self.input_1)

        time.sleep(1)

        date_field2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "DateFiledOnBefore"))
        )
        date_field2.clear()
        date_field2.send_keys(self.input_2)

        submit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "SearchSubmit"))
        )
        submit.click()

        time.sleep(3)

        
    def closed(self, reason):
        self.driver.quit()
