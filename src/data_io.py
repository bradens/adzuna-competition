import csv
import sys
import random
import json
import os
import pandas as pd
import pickle

def concatonate_files(file1, file2, output):
	files = [file1, file2]
	with open(output, 'wb') as outfile:
		for file in files:
			with open(file) as infile:
				for line in infile:
					outfile.write(line)

