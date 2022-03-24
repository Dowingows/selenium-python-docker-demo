# -*- coding: utf-8 -*-

from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

import time

def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

driver = webdriver.Chrome(options=set_chrome_options())

URL = "https://pt.wikipedia.org/wiki/Python"

driver.get(URL)
time.sleep(3)   

title = driver.find_element(By.ID, "firstHeading").text 
body = driver.find_element(By.ID, "bodyContent").text 
print("Title: ", title)     
time.sleep(3)         
print("")
print("=> Body\n", body[:200])
time.sleep(3) 
driver.stop_client()
driver.close()
driver.quit()

print("END")
