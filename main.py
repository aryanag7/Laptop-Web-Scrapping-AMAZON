import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"
req = requests.get(url)
soup= BeautifulSoup(req.text,'lxml')


quote=soup.find_all('div', {'class': 'quote'})

for i in quote:
    spans = i.find('span', attrs={'class': 'text'})
    author =i.find('small',attrs={'class':'author'})
    for span in spans:
        print(span.string)
        print(author.string)

