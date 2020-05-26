from bs4 import BeautifulSoup
with open('index.html', encoding="utf8") as html_doc:
    content = html_doc.read()
    #print(content)

soup = BeautifulSoup(content, 'html.parser')

print(soup.p.string)
print(soup.p['class'])
spi_bs4 = soup.find_all('a')
for i in spi_bs4:
    print(i.string)