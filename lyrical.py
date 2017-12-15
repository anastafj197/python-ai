# Frank Anastasia 
# We're about to get cooking

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# from selenium import webdriver 

# New Website 
my_url = 'https://www.cs.cmu.edu/~mleone/dead-lyrics.html'

# Opening connection, grabbing the page 
uClient = uReq(my_url)

# Offload content to a variable
page_html = uClient.read()

# Close client
uClient.close()

# Does html parsing 
page_soup = soup(page_html, "html.parser")

titles = page_soup.find('ul')

# Wow python is handy 
print(titles.text)

num_songs = page_soup.findAll('li')
print(len(num_songs))

# To Do 
# Extract what I need ****
# Grab song titles for test run 
# ++ Where should I put them 
# Loop through every song
# ++ Click to visit lyric page 
# ++ Grab words in song 
# ++ Place into map with associated key (num times entered)
