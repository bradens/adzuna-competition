import csv
import sys

def add_dummy_columns(input, output):
	reader = csv.reader(open(input))
	writer = csv.writer(open(output, 'wb'))

	target_index = 9
	header = reader.next()
	header.insert(target_index, 'SalaryRaw')
	header.insert(target_index, 'SalaryNormalized')
	writer.writerow(header)
	for line in reader:
		line.insert(target_index, '1')
		line.insert(target_index, '1')
		writer.writerow(line)
