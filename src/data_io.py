import json
import os

def get_paths():
	paths = json.loads(open("settings.json").read())
	for key in paths:
		paths[key] = os.path.expandvars(paths[key])
	return paths

def get_train():
	trains_path = get_paths()["trains_data_path"]
	