#Напишите парсер картинок с любого раздела сайта OZON, который их сохраняет на компьютер

import requests
from bs4 import BeautifulSoup
import re
import urllib
import os
from user_agent import generate_user_agent


path_now = os.getcwd() #get directory
URL = "https://www.ozon.ru/category/umnye-chasy-15516/"
headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
page = requests.get(URL, timeout=5, headers=headers)
name_folder = "folder"
os.mkdir(name_folder)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('img', src=re.compile('\S+.jpg'))

count = 0
for result in results:
    link = result['src']
    print(link)
    img_data = requests.get(link)
    print(img_data.content)
    with open(name_folder + "/" + str(count)+".jpg", "wb") as handler:
        handler.write(img_data.content)
    count +=1
