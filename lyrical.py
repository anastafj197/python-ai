# Frank Anastasia 
# We're about to get cooking

import re 
import urllib3
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
print()

#for url in soup.find_all('a'):
#	print(url.get('href'))

with open('100,000_Tons_of_Steel.txt','r') as f:
    for line in f:
        for word in line.split():
           print(word) 

		

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

# Entire song 
# ++ Click to visit lyric page 
# ++ Grab words in song 
# ++ Place into map with associated key (num times entered)

# Each line 
# ++ Count sylabols (sylabol counter)
# ++ Ryhme end of line (Ryhme anyalsis)
# ++ Generate a stansa 

# Add meaning 
# ++ sentiment anylisis 
# ++ Tie in a dictionary to decide parts of speach 
# ++ Anyalse for similar patterns within each song (noun, noun, adj, verb)

