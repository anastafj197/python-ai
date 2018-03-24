# Use for parts of speech
from textblob import TextBlob

def strip_blanks(txt):
	while '\n\n' in txt:
		txt = txt.replace('\n\n', '\n')
	return txt

def create_tagging_structure():	
	f = open('Dead_Combo.txt')
	text = f.read()
	text = strip_blanks(text)
	lines = text.splitlines()

	each_tag = []
	every_tag = []

	for line in lines:
		blob = TextBlob(line)

		for word, pos in blob.tags:
			each_tag.append(pos)

	print(each_tag)




create_tagging_structure()
