from lxml import etree
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import numpy as np
import requests


options = Options()
options.add_argument("--headless")
#options.add_argument("--start-maximized")
#options.add_argument("--disable-notifications")
options.add_argument("--incognito")

def page_source_from_selenium(url):
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    sleep(5)
    driver.get(url)


    total_height = int(driver.execute_script("return document.body.scrollHeight"))

    for i in range(1, total_height, 5):
        driver.execute_script("window.scrollTo(0, {});".format(i))

    page_source=driver.page_source


    print("Done Exporting Data")
    driver.close()
    driver.quit()
    print("Closed Driver")
    return page_source

def scrape_features_from_page(url):
    page_source=page_source_from_selenium(url)
    soup=bs4.BeautifulSoup(page_source,'lxml')
    dom = etree.HTML(str(soup))
    
    property_type=[i.text for i in dom.xpath("//span[@class='e2f34d59b1']") ][0]
    # if property_type!="Hotel":
    #     print ("Non-Hotel- Skipping Link")
    #     return pd.DataFrame()
    
    # else:
    hotel_name=[i.text for i in dom.xpath("//h2[@class='d2fee87262 pp-header__title']") ][0]
    _stars=[i for i in dom.xpath("//span[@data-testid='rating-circles']") ]
    stars=len(_stars[0].findall("span[@aria-hidden]"))
    location=[i.text.replace("\n","") for i in dom.xpath("//span[contains(@class, 'address')]")][0]
    review_rating=[i.text.replace("\n","") for i in dom.xpath("//div[contains(@aria-label, 'Scored')]")][0]
    location_score=[i.text.replace("\n","") for i in dom.xpath("//span[@class='review-score-badge']")][0]
    descriptions=[i.findall('p') for i in dom.xpath("//div[@id='property_description_content']")]
    description=" ".join([i.text for i in descriptions[0]])

    main_facilities=[]
    facilities_=[i for i in dom.xpath("//div[@class='hp_desc_important_facilities clearfix hp_desc_important_facilities--bui']")]

    for i in facilities_:
        #print(i.findall("div"))
        for ii in i.findall("div"):
            main_facilities.append(ii.get("data-name-en"))

    total_reviews=[i.text for i in dom.xpath("//div[@class='d8eab2cf7f c90c0a70d3 db63693c62']")][0].split(" ")[0]
    sub_ratings=[i.text for i in dom.xpath("//div[@class='ee746850b6 b8eef6afe1']")][:7]
    sub_ratings_categories=[i.text for i in dom.xpath("//span[@class='d6d4671780']")][:7]
    print(len(sub_ratings),len(sub_ratings_categories))

    sub_ratings_dict={}
    for i in range(len(sub_ratings)):
        #print(sub_ratings[i])
        #print(sub_ratings_categories[i])
        sub_ratings_dict[sub_ratings_categories[i]] = sub_ratings[i]

    #-----------------------------------------------    
    hotel_surroundings=[i.text for i in dom.xpath("//div[@class='b1e6dd8416 aacd9d0b0a']|//span[@class='b6f930dcc9']") if i.text is not None]
    hotel_surroundings_distance=[i.text for i in dom.xpath("//div[@class='db29ecfbe2 c90c0a70d3']") if i.text is not None]

    print("surroundings qc")
    print(len(hotel_surroundings), len(hotel_surroundings_distance))
    surroundings_dict = {hotel_surroundings[i]: hotel_surroundings_distance[i] for i in range(len(hotel_surroundings))}
    room_type  = [i.text.replace("\n","") for i in dom.xpath("//span[@class='hprt-roomtype-icon-link']")]


    price_list=[float(i.text.replace("\n","").strip().replace(u'₱\xa0', '').replace(",",""))
        for i in dom.xpath("//span[@class='prco-valign-middle-helper']")]

    cheapest_price=min(price_list)
    room_type_dict = {room_type[i]: price_list[i] for i in range(len(room_type))}

    facilities_groups=[i.replace("\n","") for i in dom.xpath("//div[@class='bui-title__text hotel-facilities-group__title-text']//text()") if (i!='\n') & (i.replace("\n","")!="Internet")]
    hfg=dom.xpath("//div[@class='bui-spacer--large']")
    all_facilities=[]
    for i in hfg:
        data=i.findall("div//div//div")
        facilities_per_group=[i.text.replace("\n","") for i in data if (i.text!="\n") & (i.text!=None)]
        if facilities_per_group !=[]:
            all_facilities.append(facilities_per_group)
        #print("")

    print("facilities qc")
    print(len(facilities_groups), len(all_facilities))
    # facilities_dict={facilities_groups[i]: all_facilities[i] for i in range(len(facilities_groups))}
    # internet_desc=[i.text.replace("\n","") for i in dom.xpath("//div[@class='bui-spacer--medium hotel-facilities-group__policy']") if ("wifi" in (i.text.lower()))]
    # facilities_dict["Internet"]=internet_desc



    #-----------------------------------------------   
    all_features={"hotel_name_":hotel_name,"stars":stars,
              "location":location , "location_score":location_score, 
              "review_rating":review_rating, "description":description,
              "main_facilities":main_facilities, "total_reviews":total_reviews,
              "sub_ratings":sub_ratings, "sub_ratings_categories":sub_ratings_categories,"sub_ratings_dict":sub_ratings_dict,
              "hotel_surroundings":hotel_surroundings, "hotel_surroundings_distance":hotel_surroundings_distance,"surroundings_dict":surroundings_dict,
              "room_type":room_type, "price_list":price_list,"cheapeast_price":cheapest_price, "room_type_dict":room_type_dict,
              "facilities_groups":facilities_groups,"all_facilities":all_facilities         
}


    df_all_features=pd.DataFrame({k: pd.Series([v]) for k,v in all_features.items()})
    return df_all_features


from tqdm import tqdm
df=pd.read_csv("data/all_manila_hotels_v2.csv")
links=df.url

df_hotels_consolidated=pd.DataFrame()

start_index=250
end_index=300

for count,i in tqdm(enumerate(links[start_index:end_index])):
    print("\n")
    print("Opening link- "+ str(count) + " " + str(i))
    # print(df.hotel_name[count+start_index])
    try:
        df_to_append=scrape_features_from_page(i)
        df_to_append["link"]=links[count+start_index]
        # df_to_append["hotel_name_from_all_urls"]=df.hotel_name[count+start_index]
        # df_to_append["location_from_all_urls"]=df.location[count+start_index]
        # df_to_append["distance_from_centre"]=df.distance[count+start_index]
        df_hotels_consolidated=pd.concat([df_hotels_consolidated,df_to_append])
    except Exception as e: 
        print("")
        print("Error:")
        print(str(e))
        print("Skipping due to error")
        continue
        
    print(" ")
    print("\n")

df_hotels_consolidated.to_csv('dataset_250-299.csv', index = False)