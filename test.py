# Frank Anastasia 
# We're about to get cooking

import re 
import requests
import webbrowser 
import urllib.request 

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import pynput 

#from pynput.mouse import Button, Controller

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
titles_text = titles.text
# Wow python is handy 
print(titles)
print()
print(titles_text)

#uniTitles = str(titles)

#for ul in uniTitles:
#	for li in ul:
#		a = li.find('a')
#		print(a)

# Grabs all the links on the page 
# The 1st three are not songs still 
# Working to fix that 

#songs = page_soup.find_all('a')
#print(songs.text)

# A nice place for all my links 
#links = []
#for song in songs:
#	link = song.attrs['href']
#	links.append(link)

#print(links)


# Print specific item in list 
# Prints the link to the lyrics
#print(songs[30].text)
#print(songs[30].attrs['href'])

print()

# number of song titles on the page 
#print(len(titles))

# To Do 
# Grab the right set of links (only links from the <ul>)
# ++ Click to visit lyric page 
# ++ Grab words in song 
# ++ Place into map with associated key (num times entered)
