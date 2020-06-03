#!/usr/bin/python3
from sys import argv
import os


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    filename = "add_item.json"
    my_list = load_from_json_file(filename)
except:
    my_list = []

for i in range(1, len(argv)):
    my_list.append(argv[i])

save_to_json_file(my_list, filename)
