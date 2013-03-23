import csv
import sys
from collections import defaultdict
import math
import re


def build_vw_line(line, value_index, header, target_index, index_tokenize, index_binarize):
	label = line[target_index]
	label = str(math.log(float(label)))
	new_line = []

	for i in index_tokenize:
		col = header[i]
		words = get_words(line[i])
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


def get_words(text):
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
		new_line = build_vw_line(line, value_index, header, target_index, index_tokenize, index_binarize)
		o_f.write(new_line + "\n")







