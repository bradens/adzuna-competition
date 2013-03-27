import csv
import sys
from collections import defaultdict
import math
import re
from topia.termextract import tag
from topia.termextract import extract


def build_vw_line(line, value_index, header, target_index, index_tokenize, index_binarize, keys):
	label = line[target_index]
	label = str(math.sqrt(float(label)))
	new_line = []

	for i in index_tokenize:
		col = header[i]
		words = ""
		if col == 'FullDescription':
			words = get_keywords_global(line[i], keys)
		else:
			words = get_words_bulk(line[i])
		new_item = "|%s %s" % (col, words)
		new_line.append(new_item)

	for i in index_binarize:
		col = header[i]
		value = line[i]
		value_i = value_index[i][value]
		new_item = "|%s %s" % (col, value_i)
		new_line.append(new_item)

	new_line.insert(0, label)
	new_line = " ".join(new_line)
	return new_line


def get_words_keywords(text):
	text = text.replace("'","")
	text = re.sub(r'\W+', ' ', text)
	text = text.lower()
	extractor = extract.TermExtractor()
	extractor.filter = extract.permissiveFilter
	keys = extractor(text)
	words = []
	for i in range(0, len(keys)):
		if keys[i][0] in words:
			continue
		words.append(keys[i][0])
	words = " ".join(words)
	return words

def get_keywords_global(text, keywords):
	text = text.replace("'","")
	text = re.sub(r'\W+', ' ', text)
	text = text.lower()
	text = text.split()
	words = []
	for w in text:
		if w in keywords:
			words.append(w)
	words = " ".join(words)
	return words

def get_words_bulk(text):
	text = text.replace("'","")
	text = re.sub(r'\W+', ' ', text)
	text = text.lower()
	text = text.split()
	words = []
	for w in text:
		if w in words:
			continue
		words.append(w)
	words = " ".join(words)
	return words

def load_keywords(file):
	input = open(file)
	words = []
	for line in input:
		words.append(line.rstrip('\n'))
	return words



def convert_to_vw(input, output):
	target	 	= 'SalaryNormalized'
	tokenize 	= [ 'Title', 'FullDescription', 'LocationRaw' ]
	binarize 	= [ 'LocationNormalized', 'ContractType', 'ContractTime', 'Company', 'Category', 'SourceName' ]
	drop 			= [ 'SalaryRaw' ]

	i_f = open(input)
	o_f = open(output, 'wb')
	reader = csv.reader(i_f)
	header = reader.next()

	target_index = header.index(target)
	index_tokenize = map(lambda x: header.index(x), tokenize)
	index_binarize = map(lambda x: header.index(x), binarize)
	index_drop = map(lambda x: header.index(x), drop)

	keys = load_keywords("../data/keywords-500-desc.txt")

	unique_vals = defaultdict(set)
	for line in reader:
		for i in index_binarize:
			value = line[i]
			unique_vals[i].add(value)

	value_index = defaultdict(dict)
	for i in unique_vals:
		for index, value in enumerate(sorted(list(unique_vals[i]))):
			value_index[i][value] = index + 1

	i_f.seek(0)
	reader.next()
	for line in reader:
		new_line = build_vw_line(line, value_index, header, target_index, index_tokenize, index_binarize, keys)
		o_f.write(new_line + "\n")







