#load_json.py

import json

def load_json():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)