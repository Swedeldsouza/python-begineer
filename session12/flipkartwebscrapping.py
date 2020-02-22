  #web scrapping for live html eg flipkart
from bs4 import BeautifulSoup   #html parser ,read tags from beautifulsoup
htmltxt= "<p>Hello World</p>"
soup=BeautifulSoup(htmltxt,'html.parser')        #shows text with tags
print(soup)

import requests
from bs4 import BeautifulSoup
url= 'https://www.flipkart.com/search?q=books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off '

data=requests.get(url)
plain_text=data.text
#print(plain_text)

soup=BeautifulSoup(plain_text,'html.parser')
res=soup.findAll('a',{'class':'_2cLu-l'})


for link in res:
    print(link.get('title'))
    print('-'*50)

