
from bs4 import BeautifulSoup

import requests

url = input("Ingrese una url: ")

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data,'html.parser')
print (soup.find_all('a'))

for link in soup.find_all('a'):
    print(link.get('href'))
