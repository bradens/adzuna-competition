import math
import csv
import os
import sys

def prep_final():
	o = open("../results/id-tmp", 'wb')
	reader = csv.reader(open("../data/Valid.csv"))
	header = reader.next()
	for line in reader:
		o.write(line[0] + ",\n")


def unlog():
	infile1 = open("../results/p.txt")
	infile2 = open("../results/id-tmp")
	output = open("../results/final.csv", 'wb')
	output.write("Id,SalaryNormalized\n")
	for line in infile1:
		val = line
		val = math.exp(float(val))
		output.write(infile2.readline().rstrip() + str(val) + "\n")

def square():
	infile1 = open("../results/p.txt")
	infile2 = open("../results/id-tmp")
	output = open("../results/final.csv", 'wb')
	output.write("Id,SalaryNormalized\n")
	for line in infile1:
		val = line
		val = math.pow(float(val), 2)
		output.write(infile2.readline().rstrip() + str(val) + "\n")


def main():
	if os.path.isfile("../results/id-tmp") == False:
		prep_final()

	if(sys.argv[1] == "root"):
		square()
	if(sys.argv[1] == "log"):
		unlog()


if __name__=="__main__":
	main()