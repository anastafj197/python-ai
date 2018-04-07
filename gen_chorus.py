import re
import random 
from textblob import TextBlob

def read_file(filename):
	with open(filename, "r") as file:
		contents = file.read().replace('\n\n','\n')
	return contents

data = read_file("Franklin's_Tower.txt")

# Searching for multiple lines with same lyric -> chorus
# Will yield equivelent POS patterns 	
def find_duplicates(file):
	with open(file) as f:
		seen = set()
		repeated = set()
		for line in f:
			line_lower = line.lower()
			if line_lower in seen:
				repeated.add(line)
			else:
				seen.add(line_lower)

		s = repeated
		s = list(s)

		duplicates = ' '.join(str(e) for e in s)

		#print(duplicates)

		return duplicates

# Parameters: File with song, String with the repeated line from file
# Takes in all the words from the file and splits them into POS arrays 
# Generates a common pattern by randomly pulling words from the arrays 
# that match with the POS pattern from the chorus line identified above 
# Special case for PRP$ and WP$ (Changed to PRPS & WPS)
def test_dict():
	pos_dict = {
		"CC" : set(),
		"CD" : set(),
		"DT" : set(),
		"EX" : set(),
		"FW" : set(),
		"IN" : set(),
		"JJ" : set(),
		"JJR" : set(),
		"JJS" : set(),
		"LS" : set(),
		"MD" : set(),
		"NN" : set(),
		"NNS" : set(),
		"NNP" : set(),
		"NNPS" : set(),
		"PDT" : set(),
		"POS" : set(),
		"PRP" : set(),
		"PRPS" : set(),
		"RB" : set(),
		"RBR" : set(),
		"RBS" : set(),
		"RP" : set(),
		"SYM" : set(),
		"TO" : set(),
		"UH" : set(),
		"VB" : set(),
		"VBD" : set(),
		"VBG" : set(),
		"VBN" : set(),
		"VBP" : set(),
		"VBZ" : set(),
		"WDT" : set(),
		"WP" : set(),
		"WPS" : set(),
		"WRB" : set()
	}

	f = open("Fire_On_The_Mountain.txt")
	# can remove the .lower if needed 
	text = f.read()#.lower()
	blob = TextBlob(text)
 
	for word, pos in blob.tags:
		if pos in pos_dict:
			pos_dict[pos].add(word)

	print(pos_dict)
	return pos_dict

def gen_new_chorus(pos_dict):
	sample_pos = []
	gen_chorus_line = []
	sample_chorus_line = find_duplicates("Fire_On_The_Mountain.txt")
	blob = TextBlob(sample_chorus_line)

	for word, pos in blob.tags:
		sample_pos.append(pos)

	print()
	print(sample_pos)

	# pick a random word from the array named sample_pos[i]
	for i in range(len(sample_pos)):
		#print(len(sample_pos))
		print(sample_pos[i])
		print(pos_dict[sample_pos[i]])
		print(random.sample(pos_dict[sample_pos[i]], 1))

		gen_chorus_line.append(random.sample(pos_dict[sample_pos[i]], 1))

	print()
	print(gen_chorus_line)


find_duplicates("Fire_On_The_Mountain.txt")
#split_by_pos()
pos_dict = test_dict()
gen_new_chorus(pos_dict)
