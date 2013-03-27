import sys
import csv
from collections import defaultdict
from topia.termextract import tag
from topia.termextract import extract
import re

def output_final():
	i = 0
	for w in sorted(keywords, key=keywords.get, reverse=True):
		if i >= max_words:
			break
		o_f.write(w + "\n")
		i += 1

def clean_text(text):
	text = text.replace("'","")
	text = re.sub(r'\W+', ' ', text)
	text = text.lower()
	return text

def add_keywords(keys):
	for i in range(0, len(keys)):
		keywords[keys[i][0]] += keys[i][1]


input = sys.argv[1]
output = sys.argv[2]

max_words = 1500
columns = ['FullDescription']

i_f = open(input)
o_f = open(output, 'wb')

keywords = defaultdict(int)

reader = csv.reader(i_f)
header = reader.next()

index = map(lambda x: header.index(x), columns)

for line in reader:
	for i in index:
		text = line[i]
		text = clean_text(text)
		extractor = extract.TermExtractor()
		extractor.filter = extract.permissiveFilter
		keys = extractor(text)
		add_keywords(keys)

output_final()




