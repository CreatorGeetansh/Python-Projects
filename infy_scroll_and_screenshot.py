import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# Set up Chrome options if needed
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Uncomment to run in headless mode

# Initialize the WebDriver (Selenium will manage the ChromeDriver automatically)
driver = webdriver.Chrome(options=options)

#taking screenshot automatically
driver.get("https://www.google.com/")
time.sleep(6)
search =driver.find_element("xpath","""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
search.send_keys("House of dragon")
time.sleep(3)
search.send_keys(Keys.ENTER)
time.sleep(3)
# driver.get("https://www.google.com/search?q=House+of+dragons&sca_esv=562479671&sxsrf=AB5stBhYMWhEy31husHqRYP4VhpQWqOBkA%3A1693817272399&source=hp&ei=uJn1ZNSPFrql2roPz6G28Aw&iflsig=AD69kcEAAAAAZPWnyBXZqbItlMqprdhswWIvi6MR01hd&ved=0ahUKEwjUy9WGyZCBAxW6klYBHc-QDc4Q4dUDCAk&uact=5&oq=House+of+dragons&gs_lp=Egdnd3Mtd2l6IhBIb3VzZSBvZiBkcmFnb25zMgsQLhiDARixAxiABDIIEAAYgAQYsQMyBRAAGIAEMgUQABiABDIFEC4YgAQyBxAAGIAEGAoyBxAAGIAEGAoyBRAAGIAEMgUQABiABDIFEAAYgARIjhhQ2glY2glwAXgAkAEAmAGDAqABgwKqAQMyLTG4AQPIAQD4AQL4AQGoAgrCAgcQIxjqAhgnwgINEC4YxwEY0QMY6gIYJw&sclient=gws-wiz")
a = driver.execute_script("return document.body.scrollHeight")
print(a)
driver.execute_script(f"window.scrollTo(0, {a-4500})") #scroll to a certain height
time.sleep(8)

driver.get("https://www.hbo.com/house-of-the-dragon")
driver.execute_script(f"window.scrollTo(0, {a-1500})")
time.sleep(8)
# search2 = driver.find_element("xpath","""/html/body/div[7]/div/div[12]/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[3]/div[6]/div/div/div/div/div/div[1]/div/div/a/h3""").click()
# time.sleep(10)
search3 = driver.find_element("xpath","""//*[@id="becomes-max-on-page-banner"]/div[1]/div/div[3]/img""").screenshot("C:/Users/asus/OneDrive/Pictures/Screenshots/HBO.png")
time.sleep(3)
#isi ke sath mera web scraping ka course pura hua!!!!