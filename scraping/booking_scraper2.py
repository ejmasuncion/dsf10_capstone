import bs4
import random

import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#sleep(random.randint(12, 18))

#change target page link containing city selected
#this is for Cebu
target_page = "https://www.booking.com/searchresults.en-gb.html?ss=Cebu&ssne=Baguio&ssne_untouched=Baguio&label=gen173nr-1FCAEoggI46AdIM1gEaLQBiAEBmAEJuAEXyAEM2AEB6AEB-AELiAIBqAIDuALa9-ebBsACAdICJDNiMWUxMTlhLTc3ODEtNGI3NC05MWVlLTQ5MDA0MDQzYzY5NNgCBuACAQ&sid=b3a20c12be6b3d4d9b1b0a71b11d8898&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&checkin=2022-11-25&checkout=2022-11-26&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure"
driver.get(target_page)
current_page = int(driver.find_element(by="xpath", value="//li[contains(@class, 'f32a99c8d1 ebd02eda9e')]").text)
last_page = int(driver.find_elements(by="xpath", value="//li[contains(@class, 'f32a99c8d1')]")[-1].text)


while current_page < last_page:
    time.sleep(3)
    htl_nm = driver.find_elements(By.XPATH,'//*[@id="search_results_table"]/div[2]/div/div/div/div[4]//div/h3/a/div[1]')
    for h in htl_nm:
        print(h.text)
    time.sleep(2)
    driver.find_element(by="xpath", value="//button[contains(@aria-label, 'Next page')]").click()
    current_page +=1


driver.quit()
