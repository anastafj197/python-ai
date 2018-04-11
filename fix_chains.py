import re
import random 
from textblob import TextBlob
from collections import Counter

import Markov

import lyrical

import gen_chorus

word_count = sum(len(line.split()) for line in open(r"C:\Users\owner\school\Fire_On_The_Mountain.txt"))

with open("Fire_On_The_Mountain.txt", 'r') as foo:
	lines = len(foo.readlines())
	
avg_words = int(round(word_count / lines))

#print()
#print("num words =", word_count)
#print("num lines =", lines)
#print("avg words per line =", avg_words)
#print()

message = Markov.read_file('Scarlet_Fire.txt')
chain = Markov.build_chain(message)
#message = Markov.generate_message(chain, avg_words)
#print(message)

stanza = Markov.generate_message(chain, avg_words * 40)

unique_words = lyrical.make_unique_list()
(first_rhyme, second_rhyme) = lyrical.choose_rhymes(unique_words)
lyrical.do_rhymes(first_rhyme, second_rhyme)

#print(stanza)

def play_with_string(stanza):
	print(stanza)
	nlines = stanza.count('\n')
	print(nlines)
	split_spot = int(round(nlines / 4))
	#print(split_spot)
	count = 0 
	for line in stanza.splitlines():
		count += 1
		if count == split_spot:
			# add a new line
			# fit in chorus 



play_with_string(stanza)


