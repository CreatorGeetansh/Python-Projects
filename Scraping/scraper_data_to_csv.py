import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#method 1 without oops creating vaiables and all
url= input("enter url you want to scrape: ")
webpage= requests.get(f"{url}")
soup= bs(webpage.text,"lxml")

names = soup.find_all("a", class_="title")
name_list=[]
prices = soup.find_all("h4", class_="pull-right price")
price_list= []
description = soup.find_all("p", class_="description")
description_list = []
review = soup.find_all("p", class_="pull-right")
review_list = []



for name,price,desc,rew in zip(names,prices,description,review):
    name_list.append(name.text)
    price_list.append(price.text)
    description_list.append(desc.text)
    review_list.append(rew.text)


try:
    data_sheet = pd.DataFrame({"names":name_list, "prices": price_list, "description": description_list, "Review": review_list})
    data_sheet.to_csv("scraped_data_laptops.csv")
    print("done!")
except requests.exceptions.ConnectionError:
    print("connection lost or weak internet connection!")


#method 2 by craeting my own class and using object to access it 
class scraper():
    def __init__(self,url,file_saving_name):
        webpagescarper = requests.get(f"{url}")
        soups = bs(webpagescarper.text,"lxml")

        names = soups.find_all("a", class_="title")
        name_list=[]
        prices = soups.find_all("h4", class_="pull-right price")
        price_list= []
        description = soups.find_all("p", class_="description")
        description_list = []
        review = soups.find_all("p", class_="pull-right")
        review_list = []

        for name,price,desc,rew in zip(names,prices,description,review):
           name_list.append(name.text)
           price_list.append(price.text)
           description_list.append(desc.text)
           review_list.append(rew.text)

        try:
           data_sheet = pd.DataFrame({"names":name_list, "prices": price_list, "description": description_list, "Review": review_list})
           data_sheet.to_csv(f"{file_saving_name}.csv")
           print("done!")
        except requests.exceptions.ConnectionError:
           print("connection lost or weak internet connection!")

url = input("Enter url which you wish to scrap: ")
file_name = input("name you wish to save your file: ")
scrap = scraper(url,f"{file_name}")
    
    
        