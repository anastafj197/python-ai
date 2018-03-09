# Frank Anastasia 
# Cooking with Markov

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

def read_file(filename):
	with open(filename, "r") as file:
		contents = file.read().replace('\n\n',' ')
		# this line removes newline bug but ruins the chain structure 
		contents = contents.replace('\n', ' ')
	return contents

# key: a single word
# value: a list of all subsequent words 
# Iterate throught the list pushing values for each word key
# Since we are working with word pairs start at second word
# and use the entry at index - 1 as the key  
# Returns a Markov Chain Dictionary 
def build_chain(text, chain = {}):
	words = text.split(' ')
	index = 1 
	for word in words[index:]:
		key = words[index - 1]
		if key in chain:
			chain[key].append(word)
		else:
			chain[key] = [word]
		index += 1

	return chain 

# Set desired length, assign starting word
# Walk through the chain till we reach word count 
# Returns: A random message 
def generate_message(chain, count):
	word1 = random.choice(list(chain.keys()))
	message = word1.capitalize()

	while len(message.split(' ')) < count:
		word2 = random.choice(chain[word1])
		word1 = word2
		message += ' ' + word2

	return message 

def run_markov():
	print("Generating Chain")
	print()
	message = read_file('Dead_Combo.txt')
	chain = build_chain(message)
	message = generate_message(chain, 202)
	print(message)

# Start of the syllable counter
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

# Takes in a text file, converts to lowercase, replaces punctuation
# splits into words, removes repeats, converts back to a list 
# Returns: a list of unique words from a text file 
def make_unique_list():
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
	print(unique_words)
	print()
	return unique_words

# From the unique list of words randomly selects two words to be the 
# end of line rhymes 
# Returns 2 words  
def choose_rhymes(u_list):
	print('* length of the list of all the words in the song *')
	print()
	song_len = len(u_list)
	print(song_len)
	print()
	# Grab a random word from the unique set of Fire on the Mountain 
	print('* Grabbing a random unique word from Fire on the Mountain *')
	print() 
	# Takes 1 random number between 1 and the song_len
	for x in range(1):
		rand = random.randint(1, song_len - 1)
		rand2 = random.randint(1, song_len - 1)

	print('* random position is number', rand, 'in the list *')

	first_rhyme = u_list[rand]
	second_rhyme = u_list[rand2]  

	print()
	print(first_rhyme, "is the first rhyme")
	print()
	print(second_rhyme, "is the second rhyme")
	return (first_rhyme, second_rhyme)

# Takes in a chosen word, creates a list of words that rhyme with parameter 
# Returns a word randomly from the rhyme list 
def do_rhymes(f_rhyme, s_rhyme):
	# pronouncing.rhymes(first_rhyme) returns a list of words that rhyme with first_rhyme
	print("* Printing words that rhyme with", f_rhyme, "*")
	print()
	rhyme_list_1 = pronouncing.rhymes(f_rhyme)
	print(rhyme_list_1)
	print()
	print()
	print("* Printing words that rhyme with", s_rhyme, "*")
	print()
	rhyme_list_2 = pronouncing.rhymes(s_rhyme)
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

# Takes in 2 words 
# Returns a list of words synonomous to each of the parameters 
def synonymize(f_rhyme, s_rhyme):
	print("* Generating words synonymous to", f_rhyme, "*")
	print()
	print()
	synonym_list = dictionary.synonym(f_rhyme) 
	print(synonym_list)
	print()
	print() 
	print("* Generating words synonymous to", s_rhyme, "*")
	print()
	print()
	synonym_list_2 = dictionary.synonym(s_rhyme) 
	print(synonym_list_2)
	print()
	return 0

# Used to determine the parts of speach tags for a given 
# piece of text - will be utilized in pattern matching
def pos_tagging():
	print("1. 	CC 	Coordinating conjunction")
	print("2.	CD	Cardinal number")
	print("3.	DT	Determiner")
	print("4.  	EX	Existential there")
	print("5.  	FW	Foreign word")
	print("6.  	IN	Preposition or subordinating conjunction")
	print("7.	JJ	Adjective")
	print("8.	JJR	Adjective, comparative")
	print("9.	JJS	Adjective, superlative")
	print("10.	LS	List item marker")
	print("11.	MD	Modal")
	print("12.	NN	Noun, singular or mass")
	print("13.	NNS	Noun, plural")
	print("14.	NNP	Proper noun, singular")
	print("15.	NNPS	Proper noun, plural")
	print("16.	PDT	Predeterminer")
	print("17.	POS	Possessive ending")
	print("18.	PRP	Personal pronoun")
	print("19.	PRP$	Possessive pronoun")
	print("20.	RB	Adverb")
	print("21.	RBR	Adverb, comparative")
	print("22.	RBS	Adverb, superlative")
	print("23.	RP	Particle")
	print("24.	SYM	Symbol")
	print("25.	TO	to")
	print("26.	UH	Interjection")
	print("27.	VB	Verb, base form")
	print("28.	VBD	Verb, past tense")
	print("29.	VBG	Verb, gerund or present participle")
	print("30.	VBN	Verb, past participle")
	print("31.	VBP	Verb, non-3rd person singular present")
	print("32.	VBZ	Verb, 3rd person singular present")
	print("33.	WDT	Wh-determiner")
	print("34.	WP	Wh-pronoun")
	print("35.	WP$	Possessive wh-pronoun")
	print("36.	WRB	Wh-adverb")
	print()

	# grab a specific line in the file 
	f = open('Fire_On_The_Mountain.txt')
	lines = f.readlines()
	print()

	text = lines[12]
	blob = TextBlob(text)
	print()

	print("* Parts of speech Tagging *")
	print()
	tags = []
	# blob.tags is used to find the POS a word is within a line 
	for word, pos in blob.tags:
	    print(word, pos)
	    tags.append(pos)

	print()
	print(tags)
	print()
	return 0

# Compare POS tags 
# Grab a line, count words, generate chain length of the count 

def run():
	unique_words = make_unique_list()
	(first_rhyme, second_rhyme) = choose_rhymes(unique_words)
	do_rhymes(first_rhyme, second_rhyme)
	synonymize(first_rhyme, second_rhyme)
	pos_tagging()
	run_markov()

# gibberish_stanza follows a basic POS pattern and attempts to replicate 
# Parameters: Accepts 2 random words to serve as end of line rhymes 
# Returns: A four line stanza of gibberish 
def gibberish_stanza(word, word2):
	return 0

# Accepts a list: (sentance) in the form of the parts of speech that 
# correspond to each word ex. [noun, adjetive, verb]
# runs through a loop generating a random markov chain the same length 
# as the parameter list, pulls the POS, checks if they are equal
# if not try new chain, if so -> viable sentace in the desired structure 
def find_pos_match(list):
	chain_pos_list = []
	message = read_file('Dead_Combo.txt')
	chain = build_chain(message)
	message = generate_message(chain, len(pos_list))

	blob = TextBlob(message)

	for word, pos in blob.tags:
		chain_pos_list.append(pos)  

	if pos_list == chain_pos_list: 
		print("Viable sentace structure")
		print(message)

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

# Grab a random word from the unique set of Fire on the Mountain 
print('* Grabbing a random unique word from Fire on the Mountain *')

print() 

# Gives each line as the song is written 
# To do **count syllables in each line and print**
with open('Fire_On_The_Mountain.txt','r') as f:
    for line in f:
    	count = syllable_count(line)
    	print(line, count)
    	# print(line)

print()
print()
print()
print()
print() 

run()
# To Do 
# Seperate functions into methods
# Begin the Markov Chain 

# Bugs 
# Index out of range when it cant find rhymes (Error check)
