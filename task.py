import json
import os,sys


def match_pattern(key_name):
	if "path" in key_name:
		return True
	else:
		return False

def does_the_files_exists(path_to_file):
	if(os.path.isfile(path_to_file)):
		return True
	else:
		return False

def any_file_exists(filename):
	any_false_value=1
	with open(filename,"r") as readfile:
		data=json.load(readfile)
		for keys, values in data.items():
			if(match_pattern(keys)):
				if(does_the_files_exists(values)==False):
					any_false_value=-1
			if(isinstance(values,list)):
				first_list_value=values[0]
				for nested_keys,nested_values in first_list_value.items():
					if(match_pattern(nested_keys)):
						if(does_the_files_exists(nested_values)==False):
							any_false_value=-1
					if(isinstance(nested_values,list)):
						second_list_values=nested_values[0]
						for nested_nested_keys,nested_nested_values in second_list_values.items():
							if(match_pattern(nested_nested_keys)):
								if(does_the_files_exists(nested_nested_values)==False):
									any_false_value=-1

	return any_false_value





func=lambda file_name:any_file_exists(file_name)
print(func("/opt/data/csv.json"))

#listofiles=["csv.json"]
#listofstatus=list(filter(lambda file_name:any_file_exists(file_name),listofiles))
