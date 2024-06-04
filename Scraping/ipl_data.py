import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url="https://www.iplt20.com/auction/2023"

req = requests.get(url)
print(req) #if this show status code 200 then site is scrapable
soup = bs(req.text,"lxml")

table = soup.find("table", id="t2")
heading = table.find_all("th")

head_list1 = []

for i in heading:
    head_list1.append(i.text)

#empty data frame with heading text
df1 = pd.DataFrame(columns=head_list1)
# print(df1)

# now we have successfully taken out table heading of one table
# now to find out table data using tr and td tags

rows = table.find_all("tr")

for j in rows[1:]:
    # first_td = j.find("td").find("div", class_ = "ih-pt-ic").text.strip() #to remove all those \n and use strip method for first td
    #if doesnt contain these things then continue without it 
    data = j.find_all("td")#[1:]
    row = [td.text for td in data]
    # row.insert(0,first_td)
    l = len(df1)
    df1.loc[l] = row
df1.to_csv(f"auction_data_sold_Players.csv")
print("Done!")

# tables_all = soup.find_all("table", id="t4", class_ = "ih-td-tab auction-tbl")
# print(len(tables_all))

# for tab in range(len(tables_all)-4):
#     table = soup.find_all("table", class_="ih-td-tab auction-tbl")[tab]

#     heading = table.find_all("th")

#     head_list= []
#     for i in heading:
#       head_list.append(i.text)

# #     #empty data frame with heading text
#     df = pd.DataFrame(columns=head_list)
#     print(df)

# #     #now we have successfully taken out table heading of one table
# #     # now to find out table data using tr and td tags

#     rows = table.find_all("tr")

#     for j in rows[1:]:
#       #to remove all those \n and use strip method for first td
#       first_td = rows.find_("td")[0].find("div", class_ = "ih-pt-ic").text.strip()
#       data = j.find_all("td")[1:]
#       row = [td.text for td in data]
#       row.insert(0,first_td)
#       l = len(df)
#       df.loc[l] = row
#       df.to_csv(f"auction_data_top_buys.csv")
# print("Done!")
