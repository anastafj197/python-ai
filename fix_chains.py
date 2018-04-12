import re
import random 
from textblob import TextBlob
from collections import Counter

import pronouncing

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

stanza = Markov.generate_message(chain, avg_words * 22)

unique_words = lyrical.make_unique_list()
(first_rhyme, second_rhyme) = lyrical.choose_rhymes(unique_words)
lyrical.do_rhymes(first_rhyme, second_rhyme)

#print(stanza)

def play_with_string(stanza):
	#print(stanza)
	#print()
	nlines = stanza.count('\n')
	#print("nlines =", nlines)
	split_spot = int(round(nlines / 3))
	#print()
	#print("split spot =", split_spot)
	#print()
	count_list = []
	split_list = []

	stanza_list = stanza.split(' ')

	#print(stanza_list)

	# find words that have newline characters and spots in list 
	word_count = 0
	for word in stanza_list:
		word_count += 1
		if '\n' in word:
			#print(word_count)
			count_list.append(word_count)

	print()
	#print(count_list)

	# make a list of where to add the newlines for stanza breaks 
	spot_count = 0
	for item in count_list:
		spot_count += 1
		if spot_count == split_spot:
			spot_count = 0 
			split_list.append(item)

	#print()
	#print(split_list)

	for num in split_list:
		stanza_list[num - 1] = stanza_list[num - 1].replace('\n', '\n\n')
		#print(stanza_list[num - 1])

	print()

	new_song = ' '.join(stanza_list)
	#print("******************************************************************")
	print()
	#print(new_song)
	print()
	return(new_song)

def help_lines(new_song):
	
	line_list = []
	line_list_list = []

	big_song = ""
	
	for line in new_song.splitlines():
		line_list = line.split()

		count = 0 
		for word in line_list:
			#print(word)
			if '.' in word:
				#print(".")
				line_list[count] = line_list[count].replace('.', '.\n')

			if '?' in word:
				#print("?")
				line_list[count] = line_list[count].replace('?', '?\n')

			if len(line) > 38:
				#print(len(line))
				if ',' in word:
					line_list[count] = line_list[count].replace(',', ',\n')

				if '!' in word:
					line_list[count] = line_list[count].replace('!', '!\n')

			count += 1

		song = ' '.join(line_list)

		big_song += song + '\n'

		length = len(line_list) 
		#if length >= 12:
			#line_list[int(round(length / 2))] = line_list[int(round(length / 2))] + '\n'
		#line_list_list.append(line_list)

	#print("*********************************************************")
	#print()
	#print(big_song)
	return(big_song)

	#print(line_list_list)

def word_frequency(song):
	word_freq = Counter(big_song.split()).most_common()
	#print(word_freq)

def fix_lines(big_song):
	#print("**********************************************************")

	song = ""
	list_o_list = []
	o_count = 0

	for line in big_song.splitlines():
		line_list = line.split()

		list_o_list.append(line_list)

		if len(line_list) > 0:
			end_word = line_list[len(line_list) - 1]
			#print(line_list)
			#print(end_word)



	for line in big_song.splitlines():

		#del_switch = False 

		if len(list_o_list[o_count]) == 1:
			#print("one word line")
			list_o_list[o_count].extend(list_o_list[o_count + 1])
			#del_switch = True
			#list_o_list[o_count + 1] = " "
			#print(list_o_list[o_count + 1])
			#print()

		# Dealing with extra long lines 
		if len(list_o_list[o_count]) >= 11:
			#print("**********", line)
			word_count = 0

			for word in list_o_list[o_count]:
				line = list_o_list[o_count]
				word_count += 1

				if word_count == (int(round(len(list_o_list[o_count]) / 2))) + 1:

					first_insert = line[:int(round(len(line)/2))]
					second_insert = line[int(round(len(line)/2)):]

					list_o_list[o_count] = first_insert
					list_o_list.insert( o_count + 1, second_insert)		

		o_count += 1

	for line in list_o_list:
		song_line = ' '.join(line)
		song += song_line + '\n'

	print(song)




new_song = play_with_string(stanza)
big_song = help_lines(new_song)

song = fix_lines(big_song)

word_frequency(song)

