#Сделать с помощью requests программу, в которой можно задавать
#Запрос и регион в Yandex поиске в input. Полезные ссылки она сохраняет в файле,
#В названии которого есть текст запроса и код области. Сохраняет она только ссылки с абсолютным путем типа https://

import requests
from bs4 import BeautifulSoup
import re


def find_this(q, r):
    payloads = {'text': q, 'lr': r}
    res = requests.get('https://yandex.ru/search/', params=payloads)
    soup = BeautifulSoup(res.text, 'html.parser')

    file_name = q + "_" + str(r)

    with open(file_name + ".txt", "a") as file:
        for link in soup.find_all('a', href=re.compile('^(https)')):
            file.write(link.get('href') + "\n")


query = input("Что вы хотите найти? \n")
region = input("В какой стране вы находитесь? \n")

regions = {'Россия': 225, 'Украина': 187, 'Беларусь': 149, 'Казахстан': 159}
region = region.lower().title().strip()
if region in regions.keys():
    find_this(query, regions[region])
else:
    print("К сожалению, в вашем регионе поиск запрещен!")






