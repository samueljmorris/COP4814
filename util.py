from tkinter import filedialog
from tkinter import *
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# initialize log location and format
log_handler = logging.FileHandler('SnapShare.log')
formatter = logging.Formatter('%(levelname)s  |  %(asctime)s  |  %(name)s  |  %(message)s')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)


# updates specified file with JSON data
def update_file(data, file_name):
    if not os.path.exists(file_name):
        print("File not found")
    else:
        with open(file_name, 'a') as file:
            json.dump(data, file, indent=4)


# overwrites specified file with JSON data
def overwrite_file(data, file_name):
    if not os.path.exists(file_name):
        print("File not found")
    else:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)


# prompts the user for a file
def get_filename():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("jpeg", "*.jpg"), ("PNG", "*.png"), ("all files", "*.*")))


# returns the API or secret key
def get_key(key_type):

    with open("flickr_api_key.json", 'r') as read_file:
        keys = json.load(read_file)

    return keys[key_type]
