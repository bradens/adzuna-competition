import json
import os
import pandas as pd
import pickle

def get_paths():
	paths = json.loads(open("settings.json").read())
	for key in paths:
		paths[key] = os.path.expandvars(paths[key])
	return paths

def identity(x):
	return x

# For pandas >= 10.1 this will trigger the columns to be parsed as strings
converters = { "FullDescription" : identity, "Title": identity, "LocationRaw": identity, "LocationNormalized": identity }

def get_train():
	trains_path = get_paths()["train_data_path"]
	return pd.read_csv(trains_path, converters=converters)


def get_valid():
	valid_path = get_paths()["valid_data_path"]
	return pd.read_csv(valid_path, converters=converters)

def write_predictions(predictions):
  prediction_path = get_paths()["prediction_path"]
  writer = csv.writer(open(prediction_path, "w"), lineterminator="\n")
  valid = get_valid_df()
  rows = [x for x in zip(valid["Id"], predictions.flatten())]
  writer.writerow(("Id", "SalaryNormalized"))
  writer.writerows(rows)

def save_model(model):
	out_path = get_paths()["model_path"]
	pickle.dump(model, open(out_path, "w"))

def load_model():
	in_path = get_paths()["model_path"]
	return pickle.load(open(in_path))