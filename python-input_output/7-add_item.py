#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a JSON file named 'add_item.json'.
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try to load existing items from the file
try:
    items = load_from_json_file(filename)
except (FileNotFoundError, ValueError):
    items = []

# Add command-line arguments (excluding the script name itself)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
