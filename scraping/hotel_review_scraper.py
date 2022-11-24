import bs4
import random
from lxml import etree

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
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager
import pickle

def review_details(dom,main_dict,current_page):
    country_list=[i for i in dom.xpath("//div[@class='c-review-block']//div[1]//div[@class='c-review-block__row c-review-block__guest']//div[@class='bui-avatar-block__text']//span[@class='bui-avatar-block__subtitle']//text()") if i!='\n']
    for count,i in enumerate(dom.xpath("//div[@class='c-review-block']")):
        
        try:
            country=country_list[count]
        except:
            country=""
        inner_dict={}
        #Left Block
        
        try:
            name=i.findall("div")[1].findall("div//span[@class='bui-avatar-block__title']")[0].text
        except:
            name=""
        
        try:
            room_type=i.findall("div")[1].findall("div")[0].findall("div[@class='c-review-block__row c-review-block__room-info-row']//ul/li//a//div")[0].text
        except:
            room_type=""
        
        try:
            nights_stayed=i.findall("div")[1].findall("div")[0].findall("ul[@class='bui-list bui-list--text bui-list--icon bui_font_caption c-review-block__row c-review-block__stay-date']//li//div")[0].text
        except:
            nights_stayed=""
            
        try:
            month_stayed=i.findall("div")[1].findall("div")[0].findall("ul[@class='bui-list bui-list--text bui-list--icon bui_font_caption c-review-block__row c-review-block__stay-date']//li//div//span")[0].text
        except:
            month_stayed=""
            
            
        try:
            occupant_type=i.findall("div")[1].findall("div")[0].findall("ul[@class='bui-list bui-list--text bui-list--icon bui_font_caption review-panel-wide__traveller_type c-review-block__row']//li//div")[0].text
        except:
            occupant_type=""
        
        try:
            date_reviewed=i.findall("div")[1].findall("div//span[@class='c-review-block__date']")[0].text
        except:
            date_reviewed=""
        
        try:
            review_score=i.findall("div")[1].findall("div")[1].findall("div")[0].findall("div[@class='bui-grid']")[0] \
              .findall("div[@class='bui-grid__column-1 bui-u-text-right']//div//div")[0].text
        except:
            review_score=""
        
        #Right Block
        
        try:
            short_review=i.findall("div")[1].findall("div//h3")[0].text
        except:
            short_review=""
            
        try:
            positive_review=i.findall("div")[1].findall("div")[1].findall("div")[1].findall("div//div[@class='c-review__row']" +
                            "//p//span[@class='c-review__body']")[0].text
        except:
            positive_review=""

        try:
            negative_review=i.findall("div")[1].findall("div")[1].findall("div")[1].findall("div//div[@class='c-review__row lalala']" +
                         "//p//span[@class='c-review__body']")[0].text
        except:
            negative_review=""

        inner_dict={"name":name, "room_type":room_type, "nights_stayed":nights_stayed, "month_stayed":month_stayed,
                    "occupant_type":occupant_type, "from_country":country,"review_score":review_score,
                   "date_reviewed":date_reviewed,"short_review":short_review,"positive_review":positive_review,
                    "negative_review":negative_review
                   }

        main_dict["From Page "+str(current_page)+", Person- "+ str(count+1)]=inner_dict


def get_review_body(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    driver.maximize_window()


    time.sleep(3)
    driver.execute_script('window.scrollTo(0, 100)')
        
    #click Read all reviews button
    driver.find_element(by="xpath", value="//a[@data-target= 'hp-reviews-sliding']").click()
    #Switch to review window
    driver.switch_to.window(driver.window_handles[0])

    soup = BeautifulSoup(driver.page_source,"html.parser")

    #get min and max pages
    current_page = 1
    time.sleep(3)
    
    all_pageList = driver.find_elements(by="xpath",value="//a[contains(@class,'bui-pagination__link')]")

    try:
        last = driver.find_element(by="xpath", value="//*[@id='review_list_page_container']/div[4]/div/div[1]/div/div[2]/div/div[7]/a/span[2]").text
        last2 = last.split(" ")
        last_page = int(last2[1])
    except Exception as e: 
        if len(all_pageList) == 2:
            last = driver.find_element(by="xpath", value="//*[@id='review_list_page_container']/div[4]/div/div[1]/div/div[2]/div/div[2]/a/span[2]").text
            last2 = last.split(" ")
            last_page = int(last2[1]) + 1
        elif len(all_pageList) == 3:
            last = driver.find_element(by="xpath", value="//*[@id='review_list_page_container']/div[4]/div/div[1]/div/div[2]/div/div[3]/a/span[2]").text
            last2 = last.split(" ")
            last_page = int(last2[1]) + 1
        elif len(all_pageList) == 4:
            last = driver.find_element(by="xpath", value="//*[@id='review_list_page_container']/div[4]/div/div[1]/div/div[2]/div/div[4]/a/span[2]").text
            last2 = last.split(" ")
            last_page = int(last2[1]) + 1
        elif len(all_pageList) == 5:
            last = driver.find_element(by="xpath", value="//*[@id='review_list_page_container']/div[4]/div/div[1]/div/div[2]/div/div[5]/a/span[2]").text
            last2 = last.split(" ")
            last_page = int(last2[1]) + 1
        elif len(all_pageList) == 6:
            last = driver.find_element(by="xpath", value="//*[@id='review_list_page_container']/div[4]/div/div[1]/div/div[2]/div/div[6]/a/span[2]").text
            last2 = last.split(" ")
            last_page = int(last2[1]) + 1
        elif len(all_pageList) == 1:
            last_page = current_page
    
    try:
        print("Total Pages- " + str(last_page))
    except Exception as e: 
        last_page=1
        print("Total Pages- " + str(last_page))
    review_body=[]
    main_dict={}
    while current_page <= last_page:
        print("Current Page- " +str(current_page))
        time.sleep(3)
        
        page_source=driver.page_source
        soup=bs4.BeautifulSoup(page_source,'lxml')
        dom = etree.HTML(str(soup))
        
        
        review_details(dom,main_dict,current_page)
        
        time.sleep(3)
        if current_page<last_page:
            while True:
                try:
                    driver.find_element(by="xpath", value="//a[contains(@class, 'pagenext')]").click()
                    break
                except:    
                    print("Click Error-Trying Again")
                    time.sleep(5)
                    pass
                  
        current_page +=1
    
    driver.quit()
    dict_to_df={"url":url,"All_reviews":main_dict}
    df=pd.DataFrame({k: pd.Series([v]) for k,v in dict_to_df.items()})
    return df


def scrape_hotel_reviews(urls, start_index, end_index):
    # df=pd.read_csv("data/consolidated_urls.csv")
    df=pd.read_csv(urls)
    links=df.link

    df_hotels_consolidated=pd.DataFrame()

    start_index=start_index
    end_index=end_index

    for count,i in tqdm(enumerate(links[start_index:end_index])):
        print("Opening link- "+ str(count) + " " + str(i))
        #print(df.hotel_name[count+start_index])
        #try:
        df_to_append=get_review_body(i)
        df_hotels_consolidated=pd.concat([df_hotels_consolidated,df_to_append])
        
    print(" ")

    df_hotels_consolidated.to_csv('reviews_'+ str(start_index) + '-' + str(end_index-1) +'.csv', index = False)
    pickle.dump(df_hotels_consolidated, open('reviews_'+ str(start_index) + '-' + str(end_index-1) +'.pkl', "wb")) #to retain datatypes