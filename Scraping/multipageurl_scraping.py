#in this program we will learn how to extract all the url of next pages in a multipage website like flipcart

import pandas as pd
import requests
from bs4 import BeautifulSoup as beau

#if the web site have multiple pages and all pages have same url but just page no. is different at the end... for that
pages = int(input("Enter how many pages you wish to scrape:"))
item_list = []
price_list = []
desc_list = []

for i in range(2,pages+2): #ab ye page 2 se scrape kr lega aage ka sara data and apne aap csv files me save krta chlega page wise
    url = "https://www.hdfcbank.com/personal/pay/cards"+str(i)
    req = requests.get(url)
    soup = beau(req.text,"lxml")
    new_page_url = soup.find("a", class_ = "_1LKTO3").get("href")
    new_soup = "https://www.flipkart.com" + new_page_url
    items = soup.find_all("div", class_ = "_4rR01T")
    prices = soup.find_all("div", class_ = "_30jeq3 _1_WHN1")
    description = soup.find_all("ul", class_ = "_1xgFaf")

    for item,price,desc in zip(items,prices,description):
        item_list.append(item.text)
        price_list.append(price.text)
        desc_list.append(desc.text)
        
data_sheet = pd.DataFrame({"items": item_list, "prices": price_list, "description": desc_list})
data_sheet.to_csv(f"flipcart_mobiles_data_page.csv")
print("Work done successfully!")

#but what if every page has a different url.... hmm that's tricky and intersting as well but will try to do it:>