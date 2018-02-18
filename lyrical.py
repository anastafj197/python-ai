# Frank Anastasia 
# We're about to get cooking

import re 
import random 
import urllib3
import webbrowser 
import urllib.request 

# Use for the rhymes 
import pronouncing

# Use for parts of speech
from textblob import TextBlob

# Use for synonyms 
from PyDictionary import PyDictionary
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import pynput 

#from pynput.mouse import Button, Controller

# creating a dictionary instance which can take words as arguments
dictionary = PyDictionary()

# New Website 
my_url = 'https://www.cs.cmu.edu/~mleone/dead-lyrics.html'

# Opening connection, grabbing the page 
uClient = uReq(my_url)

# Offload content to a variable
page_html = uClient.read()

# Close client
uClient.close()

# Does html parsing 
page_soup = soup(page_html, "lxml")

titles = page_soup.find('ul')
titles_text = titles.text

# Start of the syllable counter
print("* syllable counter *")

# syllable_count uses vowels to determine syllables 
# Parameters: Accepts a word or words 
# Returns: A count of all the syllables 
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

# gibberish_stanza follows a basic POS pattern and attempts to replicate 
# Parameters: Accepts 2 random words to serve as end of line rhymes 
# Returns: A four line stanza of gibberish 
def gibberish_stanza(word, word2):
	return 0

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

file = open('Fire_On_The_Mountain.txt', 'r')
# .lower() returns a version with all upper case characters replaced with lower case characters.
text = file.read().lower()
file.close()
# replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
text = re.sub('[^a-z\ \']+', " ", text)
# Split the song by words, remove repeats, convert back to a list 
unique_words = list(text.split())
unique_words = set(unique_words)
unique_words = list(unique_words)

print()
print('* length of the list of all the words in the song *')
print()
song_len = len(unique_words)
print(song_len)
print()
print(unique_words)
print()

# Grab a random word from the unique set of Fire on the Mountain 
print('* Grabbing a random unique word from Fire on the Mountain *')

print() 

# Takes 1 random number between 1 and the song_len
for x in range(1):
	rand = random.randint(1, song_len - 1)
	rand2 = random.randint(1, song_len - 1)

print('* random position is number', rand, 'in the list *')

first_ryhme = unique_words[rand]
second_ryhme = unique_words[rand2]  

print()
print(first_ryhme, "is the first ryhme")
print()
print(second_ryhme, "is the second ryhme")
print()
print()
# Gives each line as the song is written 
# To do **count syllables in each line and print**
with open('Fire_On_The_Mountain.txt','r') as f:
    for line in f:
    	count = syllable_count(line)
    	print(line, count)
    	# print(line)

# grab a specific line in the file 
f = open('Fire_On_The_Mountain.txt')
lines = f.readlines()

print()
# specific line syl count 
#print(lines[25])
#count = syllable_count(lines[25])
#print(count)

text = lines[12]
blob = TextBlob(text)

print()
print("* Parts of speech Tagging *")
print()

# blob.tags is used to find the POS a word is within a line 
print(blob.tags) 

print()
print()

# pronouncing.rhymes(first_ryhme) returns a list of words that ryhme with first_ryhme
print("* Printing words that ryhme with", first_ryhme, "*")
print()
ryhme_list = pronouncing.rhymes(first_ryhme)
print(ryhme_list)

# Picking a random position in ryhme_list
# Which will ryhme with first_ryhme
ryhme_list_len = len(ryhme_list)

for x in range(1):
	rand_ryhme = random.randint(1, ryhme_list_len - 1)

first_ryhmer = ryhme_list[rand_ryhme] 
print()
print("* Selected ryhmer *")
print()
print(first_ryhmer)

print()
print("* Generating words synonymous to", first_ryhme, "*")
print()
print()

synonym_list = dictionary.synonym(first_ryhme) 
print(synonym_list)

# Grabs all the links on the page 
# The 1st three are not songs still 
# Working to fix that 

#songs = page_soup.find_all('a')
#print(songs.text)

# A nice place for all my links 
# links = []
# for song in songs:
#	link = song.attrs['href']
#	links.append(link)

#print(links)


# Print specific item in list 
# Prints the link to the lyrics
#print(songs[30].text)
#print(songs[30].attrs['href'])

print()

# number of song titles on the page 
# print(len(titles))

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
