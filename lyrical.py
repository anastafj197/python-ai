# Frank Anastasia 
# We're about to get cooking

import re 
import urllib3
import webbrowser 
import urllib.request 

# Use for the rhymes 
import pronouncing

# Use for parts of speech
from textblob import TextBlob

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

# Start of the syllable counter
print("* syllable counter *")

def syllable_count(word):
	word = word.lower()
	count = 0 
	vowels = "ayeiou"
	if word in vowels:
		count += 1
	for index in range(1, len(word)):
		if word[index] in vowels and word[index - 1] not in vowels:
			count += 1 
			if word.endswith("e"):
				count -= 1
	if count == 0:
		count += 1 
	return count 

# This prints the name with the url 
# Along with all the rest of the li in the <ul> 
print(titles) 
print()

# This only prints the names of all the songs
print(titles_text) 
print()



# Gives each word of a specific saved text file on a new line 
with open('Fire_On_The_Mountain.txt','r') as f:
    for line in f:
        for word in line.split():
           print(word) 

print()

# Gives each line as the song is written 
# To do **count syllables in each line and print**
with open('Fire_On_The_Mountain.txt','r') as f:
    for line in f:
    	count = syllable_count(line)
    	print("{} {}".format(line, count))
    	# print(line)

# grab a specific line in the file 
f = open('Fire_On_The_Mountain.txt')
lines = f.readlines()
print(lines[25])
count = syllable_count(lines[25])
print(count)

text = lines[24]
blob = TextBlob(text)
print(blob.tags) 

print()
print()
print(pronouncing.rhymes("tree"))
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
# ++ Count syllable 
# ++ Ryhme end of line (Ryhme anyalsis)
# ++ Generate a stansa 


print() 


#print(syllable_count('fire')) 

# Add meaning 
# ++ sentiment anylisis 
# ++ Tie in a dictionary to decide parts of speach 
# ++ Anyalse for similar patterns within each song (noun, noun, adj, verb)
