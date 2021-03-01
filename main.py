import requests
from bs4 import BeautifulSoup
import csv


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

url = "https://www.amazon.in/s?k=laptops&ref=nb_sb_noss_2"
req = requests.get(url,headers=headers).text
soup= BeautifulSoup(req,'lxml')

Names=[]
Prices=[]

for i in soup.find_all('a',class_='a-link-normal a-text-normal'):
    string1=i.text
    Names.append(string1.strip())

for i in soup.find_all('span',class_='a-price-whole'):
    string2=i.text
    Prices.append(string2)


file_name = 'Laptops.csv'

with open(file_name,'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.no','Laptop Name','Prices'])

    for i in range(len(Names)):
        writer.writerow([i, Names[i], Prices[i]])



