#load_json.py

import json

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)