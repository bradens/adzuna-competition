import math
import csv

def prep_final():
	o = open("../results/id-tmp", 'wb')
	reader = csv.reader(open("../data/Valid.csv"))
	header = reader.next()
	for line in reader:
		o.write(line[0] + ",\n")


def unlog(input):
	infile1 = open(input)
	infile2 = open("../results/id-tmp")
	output = open("../results/final.csv", 'wb')
	output.write("Id,SalaryNormalized\n")
	for line in infile1:
		val = line
		val = math.exp(float(val))
		output.write(infile2.readline().rstrip() + str(val) + "\n")

def squareroot(input):
	infile1 = open(input)
	infile2 = open("../results/id-tmp")
	output = open("../results/final.csv", 'wb')
	output.write("Id,SalaryNormalized\n")
	for line in infile1:
		val = line
		val = math.sqrt(float(val))
		output.write(infile2.readline().rstrip() + str(val) + "\n")