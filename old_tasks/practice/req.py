import requests
from bs4 import BeautifulSoup


payloads = {'text':'чайник', 'lr':149}
r = requests.get('https://google.com/', params=payloads)
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())

with open("result.txt", "a") as file:
    for link in soup.find_all("a"):
        file.write(link.get('href') + "\n")

