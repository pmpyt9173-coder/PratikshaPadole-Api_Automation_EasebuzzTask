import json
import os

def save_json(data, file):

    os.makedirs(os.path.dirname(file), exist_ok=True)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)