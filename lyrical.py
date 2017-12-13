# Frank Anastasia 

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

from selenium import webdriver 

my_url = 'https://lyrics.az/grateful-dead/allsongs.html'

# opening connection, grabbing the page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# Does html parsing 
page_soup = soup(page_html, "html.parser")
