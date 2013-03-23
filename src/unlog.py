import math

def unlog(input, output):
	infile = open(input)
	outfile = open(output, 'wb')
	for line in infile:
		val = line
		val = math.exp(float(val))
		outfile.write(str(val) + "\n")