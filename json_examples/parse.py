import json
from pprint import pprint

with open('json_data') as data_file:    
    data = json.load(data_file)
pprint(data)
