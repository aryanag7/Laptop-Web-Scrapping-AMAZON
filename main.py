import requests
from bs4 import BeautifulSoup


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

url = "https://quotes.toscrape.com/"
req = requests.get(url,headers=headers).text
soup= BeautifulSoup(req,'lxml')

Names=[]
Prices=[]

for i in soup.find_all('a',class_='a-link-normal a-text-normal'):
    string=i.text
    Names.append(i.strip())

for each in Names:
    print(each)



