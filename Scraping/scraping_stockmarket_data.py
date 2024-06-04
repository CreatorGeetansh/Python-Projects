#in this program we will be storing tabular data form a web site of stock market with some different methods..
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url="https://ticker.finology.in/market"

req = requests.get(url)
# print(req) if this show status code 200 then site is scrapable
soup = bs(req.text,"lxml")

table1 = soup.find("table", class_="table table-sm table-hover screenertable")

heading1 = table1.find_all("th")

head_list1 = []
for i in heading1:
    head_list1.append(i.text)

#empty data frame with heading text
df1 = pd.DataFrame(columns=head_list1)

# now we have successfully taken out table heading of one table
# now to find out table data using tr and td tags

rows = table1.find_all("tr")

for j in rows[1:]:
    data = j.find_all("td")
    row = [td.text for td in data]
    # print(row)
    l = len(df1)
    df1.loc[l] = row

print(df1)

# #for second table of low price 

# table2 = soup.find_all("table", class_="table table-sm table-hover screenertable")[1]

# heading2 = table2.find_all("th")

# head_list2 = []

# for i in heading2:
#     head_list2.append(i.text)

# #empty data frame with heading text
# df2 = pd.DataFrame(columns=head_list2)

# #now we have successfully taken out table heading of one table
# # now to find out table data using tr and td tags

# rows = table2.find_all("tr")

# for j in rows[1:]:
#     data = j.find_all("td")
#     row = [td.text for td in data]
#     # print(row)
#     l = len(df2)
#     df2.loc[l] = row

# print(df2)

#lets try to scrape all the table at once using for loop bit difficult at first lets get started
#ek web page me jitne bhi tables h sare scrap ho skte h ab ek sath isn't amazing i ahve craeted that software.

# tables_all = soup.find_all("table", class_="table table-sm table-hover screenertable")

# for tab in range(len(tables_all)):
#     table = soup.find_all("table", class_="table table-sm table-hover screenertable")[tab]

#     heading = table.find_all("th")

#     head_list= []
#     for i in heading:
#       head_list.append(i.text)

#     #empty data frame with heading text
#     df = pd.DataFrame(columns=head_list)

#     #now we have successfully taken out table heading of one table
#     # now to find out table data using tr and td tags

#     rows = table.find_all("tr")

    # for j in rows[1:]:
    #   data = j.find_all("td")
    #   row = [td.text for td in data]
    #   # print(row)
    #   l = len(df)
    #   df.loc[l] = row
    # print(df)
    # df.to_csv(f"file_data{tab}.csv")


