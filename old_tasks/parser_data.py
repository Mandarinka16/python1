import requests
from bs4 import BeautifulSoup
import re
import urllib3
import os

#[\w.\]+@\w+\.\w+
# (\d{1,3}\.){3}\d{1,3}\
# .+(?=:)

path_now = os.getcwd() #get directory
URL = "https://www.ozon.ru/category/playstation-31719/"
URL = URL.strip()
name_folder = "folder"
os.mkdir(name_folder)
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('img', src=re.compile('\S+(.jpg)'))
#print(soup.prettify())
#print(results)
#print(type(results))
print(len(results))


count = 0

for result in results:
    link = result['src']
    print(link)
    img_data = requests.get(link)
    print(img_data.content)
    with open(name_folder + "/" + str(count)+".jpg", "wb") as handler:
        handler.write(img_data.content)
    count +=1