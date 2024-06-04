from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# Initialize the WebDriver (Selenium will manage the ChromeDriver automatically)
driver = webdriver.Chrome(options=options)
# def clicking_button_by_xpath(url,xpath_path):

#     driver.get(url) #url of the scraping pageby xpath or class. default vale id hai iski.
    
#     time.sleep(3)
#     #new selenium module me define krna pdega find kaise krna h 
#     driver.find_element("xpath",f"""{xpath_path}""").click()


# #this will go to youtube website and just after 3 sec it will click on search button
# x=time.time()
# clicking_button_by_xpath("https://www.youtube.com/","""/html/body/ytd-app/div[1]/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[2]/a""")
# y = time.time()
# print(f"time for execution of this program is {y-x}sec.")

#now we have to fill any login form using selenium.. automatically

#driver will open google website and search for input area then the keys will send whatever written in it to the text area and then press enter automatically.
def main():
    driver.get("https://www.google.com")
    time.sleep(5)
    search = driver.find_element("xpath","""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
    search.send_keys("edx login")
    time.sleep(3)
    search.send_keys(Keys.ENTER)
    time.sleep(3)
    #opening edx login page.

    #sign in credentials
    driver.get("https://authn.edx.org/login")
    time.sleep(9)
    username_input= driver.find_element("xpath","/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/div[1]/div[1]/input")
    username_input.send_keys("Creator_Geetansh")
    time.sleep(9)


    z = "SOqvA-B_WD3ebcB7_MBbP" #my encrypted password

    #password decryptor
    if(len(z)==3):
      print(f"{z[2]+z[1]+z[0]}")
    elif(len(z)==2):
      print(f"{z[1]+z[0]}")
    elif(len(z) == 1):
      print(f"{z[0]}")
    else: 
      x = z[3:len(z)-4]
      b = x[::-1]
      password = z[len(z)-4] + b

    password_input= driver.find_element("xpath","""/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/div[2]/div/input""")
    password_input.send_keys(f"{password}")
    time.sleep(3)

    #clicking the sign in button
    driver.find_element("xpath","""/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/form/button""").click()
    time.sleep(30)


if __name__ == '__main__':
   main()