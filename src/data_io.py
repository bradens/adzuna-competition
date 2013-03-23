import csv
import sys
import random
import json
import os
import pandas as pd
import pickle

def get_paths():
	paths = json.loads(open("settings.json").read())
	for key in paths:
		paths[key] = os.path.expandvars(paths[key])
	return paths

def get_train_path():
	return str(get_paths()["train_data_path"])


def get_valid_path():
	return str(get_paths()["valid_data_path"])

