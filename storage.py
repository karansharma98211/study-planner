# storage.py
# Handles saving and loading all data

import json

FILE = "data.json"

def save_data(subjects, sessions):
    data = {
        "subjects": subjects,
        "sessions": sessions
    }
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("Data saved.")

def load_data():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return data["subjects"], data["sessions"]
    except FileNotFoundError:
        return {}, []