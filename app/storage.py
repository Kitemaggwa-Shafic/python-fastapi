# storage python file for our data to use, and it store data and load data
# keep data in json format

from pathlib import Path
import json


DATA_DIR = Path("date")
DATA_FILE = DATA_DIR/"issues.json"

#fucntion for loading our saved data
def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
    return []


# function for saving data, takes in data
def save_data(data):
    #we first create a data dir if it doesnt exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    


