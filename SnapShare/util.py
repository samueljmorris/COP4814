import tkinter
import json
import os
import custom_logs as cl
import tkinter as tk
from tkinter import filedialog
dialogs = tk.Tk()
log = cl.CLog(module="util", file="SnapShare.log")


# updates specified file with JSON data
def update_file(data, file_name):
    if not os.path.exists(file_name):
        print('"' + file_name + '"' + " not found")
        log.logger.error('"' + file_name + '"' + " not found")
    else:
        with open(file_name, 'a') as file:
            json.dump(data, file, indent=4)
    log.logger.info("Save (append) completed to '"'' + file_name + "'")


# overwrites specified file with JSON data
def overwrite_file(data, file_name):
    if not os.path.exists(file_name):
        print('"' + file_name + '"' + " not found")
        log.logger.error('"' + file_name + '"' + " not found")
    else:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
    log.logger.info("Save (overwrite) completed to '"'' + file_name + "'")


# prompts the user for a file
def get_filename():
    file_name = dialogs.filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("jpeg", "*.jpg"), ("PNG", "*.png"), ("all files", "*.*")))
    if not file_name:    # user canceled
        log.logger.info("User canceled open dialog")
    else:
        return file_name


def set_filename():
    file_name = dialogs.filename = filedialog.asksaveasfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("jpeg", "*.jpg"), ("PNG", "*.png"), ("all files", "*.*")),
        )
    if not file_name:    # user canceled
        log.logger.info("User canceled save dialog")
    else:
        return file_name


# returns the API or secret key
def get_key(key_type):
    if not os.path.exists("flickr_api_key.json"):
        print("File not found")
        log.logger.error("API key file not found")
    with open("flickr_api_key.json", 'r') as read_file:
        keys = json.load(read_file)

    return keys[key_type]

