import csv
import sys

def add_dummy_column(input, output):
	reader = csv.reader(open(input))
	writer = csv.writer(open(output, 'wb'))

	header = reader.next()
	target_index = 9
	for line in reader:
		line.insert(target_index, '1')
		line.insert(target_index, '1')
		writer.writerow(line)
