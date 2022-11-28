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


#change target page link containing city selected
#this is for Manila
target_page = "https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaLQBiAEBmAEJuAEXyAEM2AEB6AEB-AELiAIBqAIDuALa9-ebBsACAdICJDNiMWUxMTlhLTc3ODEtNGI3NC05MWVlLTQ5MDA0MDQzYzY5NNgCBuACAQ&sid=b3a20c12be6b3d4d9b1b0a71b11d8898&aid=304142&checkin=2022-12-01&checkout=2022-12-02&dest_id=-2437894&dest_type=city&latitude=14.596765518188477&longitude=120.98368072509766&sb_travel_purpose=leisure&nflt=ht_id%3D204&order=popularity&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&age=&req_age=&shw_aparth=0"
driver.get(target_page)

#get current and last page
current_page = int(driver.find_element(by="xpath", value="//li[contains(@class, 'f32a99c8d1 ebd02eda9e')]").text)
last_page = int(driver.find_elements(by="xpath", value="//li[contains(@class, 'f32a99c8d1')]")[-1].text)

#get all hotel urls (all pages)
hotel_url=[]
while current_page < last_page:
    time.sleep(3)
    hotels = driver.find_elements(by="xpath", value="//a[contains(@class, 'e13098a59f')]")
    for h in hotels:
        hotel = h.get_attribute("href")
        hotel_url.append(hotel)

    time.sleep(2)
    driver.find_element(by="xpath", value="//button[contains(@aria-label, 'Next page')]").click()
    current_page +=1

#for checking only: write to csv
df = pd.DataFrame (hotel_url, columns = ['url'])
df.to_csv('manila_url2.csv',index=False)

driver.quit()
