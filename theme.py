import re
import random 
from textblob import TextBlob

def determine_theme(file):
	nouns = []
	proper_nouns = []
	with open(file, 'r') as f:
		for line in f:
			blob = TextBlob(line)
			for word, pos in blob.tags:
				if pos == "NN" or pos == "NNS":
					nouns.append(word)
				if pos == "NNP" or pos == "NNPS":
					proper_nouns.append(word)

	nouns = set(nouns)
	nouns = list(nouns)
	proper_nouns = set(proper_nouns)
	proper_nouns = list(proper_nouns)

	print("Nouns")
	print()
	print(nouns)
	print()
	print("Proper_nouns")
	print()
	print(proper_nouns)
	print()
	print("Song Title")
	print()
	print(random.choice(proper_nouns), random.choice(nouns))


determine_theme("Dead_Combo.txt")
