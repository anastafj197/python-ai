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
def split_by_pos():
	CC, CD, DT, EX, FW, IN, JJ, JJR, JJS, LS, MD, NN, NNS, NNP, NNPS, PDT, POS, PRP, PRPS, RB, RBR, RBS, RP, SYM, TO, UH, VB, VBD, VBG, VBN, VBP, VBZ, WDT, WP, WPS, WRB = ([] for i in range(36))
	
	f = open("Franklin's_Tower.txt")
	text = f.read()
	blob = TextBlob(text)
	# This is dirty needs redesign change structure to 2d array and loop through that 
	for word, pos in blob.tags:
		if pos == "CC":
			CC.append(word)
		elif pos == "CD":
			CD.append(word)
		elif pos == "DT":
			DT.append(word)
		elif pos == "EX":
			EX.append(word)
		elif pos == "FW":
			FW.append(word)
		elif pos == "IN":
			IN.append(word)
		elif pos == "JJ":
			JJ.append(word)
		elif pos == "JJR":
			JJR.append(word)
		elif pos == "JJS":
			JJS.append(word)
		elif pos == "LS":
			LS.append(word)
		elif pos == "MD":
			MD.append(word)
		elif pos == "NN":
			NN.append(word)
		elif pos == "NNS":
			NNS.append(word)
		elif pos == "NNP":
			NNP.append(word)
		elif pos == "NNPS":
			NNPS.append(word)
		elif pos == "PDT":
			PDT.append(word)
		elif pos == "POS":
			POS.append(word)
		elif pos == "PRP":
			PRP.append(word)
		elif pos == "PRPS":
			PRPS.append(word)
		elif pos == "PRB":
			PRB.append(word)
		elif pos == "RBR":
			RBR.append(word)
		elif pos == "RBS":
			RBS.append(word)
		elif pos == "RP":
			RP.append(word)
		elif pos == "SYM":
			SYM.append(word)
		elif pos == "TO":
			TO.append(word)
		elif pos == "UH":
			UH.append(word)
		elif pos == "VB":
			VB.append(word)
		elif pos == "VBD":
			VBD.append(word)	
		elif pos == "VBG":
			VBG.append(word)
		elif pos == "VBN":
			VBN.append(word)
		elif pos == "VBP":
			VBP.append(word)
		elif pos == "VBZ":
			VBZ.append(word)
		elif pos == "WDT":
			WDT.append(word)
		elif pos == "WP":
			WP.append(word)
		elif pos == "WPS":
			WPS.append(word)
		elif pos == "WRB":
			WRB.append(word)


	#print(VB)


def test_dict():
	pos_dict = {
				"CC" : [],
				"CD" : [],
				"DT" : [],
				"EX" : [],
				"FW" : [],
				"IN" : [],
				"JJ" : [],
				"JJR" : [],
				"JJS" : [],
				"LS" : [],
				"MD" : [],
				"NN" : [],
				"NNS" : [],
				"NNP" : [],
				"NNPS" : [],
				"PDT" : [],
				"POS" : [],
				"PRP" : [],
				"PRPS" : [],
				"RB" : [],
				"RBR" : [],
				"RBS" : [],
				"RP" : [],
				"SYM" : [],
				"TO" : [],
				"UH" : [],
				"VB" : [],
				"VBD" : [],
				"VBG" : [],
				"VBN" : [],
				"VBP" : [],
				"VBZ" : [],
				"WDT" : [],
				"WP" : [],
				"WPS" : [],
				"WRB" : []
	}

	f = open("Franklin's_Tower.txt")
	text = f.read()
	blob = TextBlob(text)
 
	for word, pos in blob.tags:
		

def gen_new_chorus():
	sample_pos = []
	gen_chorus_line = []
	sample_chorus_line = find_duplicates("Franklin's_Tower.txt")
	blob = TextBlob(sample_chorus_line)

	for word, pos in blob.tags:
		sample_pos.append(pos)

	print(sample_pos)

	# pick a random word from the array named sample_pos[i]
	for i in range(len(sample_pos)):
		print(random.choice(sample_pos[i]))
		gen_chorus_line.append(random.choice(sample_pos[i]))

	print(gen_chorus_line)


find_duplicates("Franklin's_Tower.txt")
split_by_pos()
gen_new_chorus()
