# Frank Anastasia 
# We're about to get cooking

import re 
import sys
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

first_rhyme = unique_words[rand]
second_rhyme = unique_words[rand2]  

print()
print(first_rhyme, "is the first rhyme")
print()
print(second_rhyme, "is the second rhyme")
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

# pronouncing.rhymes(first_rhyme) returns a list of words that rhyme with first_rhyme
print("* Printing words that rhyme with", first_rhyme, "*")
print()
rhyme_list_1 = pronouncing.rhymes(first_rhyme)
print(rhyme_list_1)
print()
print()
print("* Printing words that rhyme with", second_rhyme, "*")
print()
rhyme_list_2 = pronouncing.rhymes(second_rhyme)
print(rhyme_list_2)

# Picking a random position in rhyme_list
# Which will rhyme with first_rhyme
rhyme_list_len_1 = len(rhyme_list_1)
rhyme_list_len_2 = len(rhyme_list_2)

for x in range(1):
	rand_rhyme_1 = random.randint(1, rhyme_list_len_1 - 1)
	rand_rhyme_2 = random.randint(1, rhyme_list_len_2 - 1)

first_rhymer = rhyme_list_1[rand_rhyme_1] 
second_rhymer = rhyme_list_2[rand_rhyme_2]

print()
print("* Selected rhymers *")
print()
print("1", first_rhymer)
print("2", second_rhymer)
print()
print("* Generating words synonymous to", first_rhyme, "*")
print()
print()

synonym_list = dictionary.synonym(first_rhyme) 

print(synonym_list)
print()
print() 

print("* Generating words synonymous to", second_rhyme, "*")
print()
print()

synonym_list_2 = dictionary.synonym(second_rhyme) 

print(synonym_list_2)
print()
print() 


# To Do 
# Seperate functions into methods
# Begin the Markov Chain 

# Bugs 
# Index out of range when it cant find rhymes (Error check)
