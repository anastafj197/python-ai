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

# To Do 
# Click view all songs 
# Grab song titles for test run 
# Loop through every song
# + + Click to visit lyric page 
# + + Grab words in song 
# + + Place into map with associated key (num times entered)
