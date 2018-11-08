import json
import os
import tkinter as tk
from tkinter import filedialog
import custom_logs as cl
log = cl.CLog(module=__name__, file="SnapShare.log")
dialogs = tk.Tk()

log.logger.info("Util started")


# updates specified file with JSON data
def update_file_json(data, file_name):
    if not os.path.exists(file_name):
        print('"' + file_name + '"' + " not found")
        log.logger.error('"' + file_name + '"' + " not found")
    else:
        with open(file_name, 'a') as file:
            json.dump(data, file, indent=4)
    log.logger.info("Save (append) completed to '"'' + file_name + "'")


# overwrites specified file with JSON data
def overwrite_file_json(data, file_name):
    if not os.path.exists(file_name):
        print('"' + file_name + '"' + " not found")
        log.logger.error('"' + file_name + '"' + " not found")
    else:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
    log.logger.info("Save (overwrite) completed to '"'' + file_name + "'")


# prompts the user for a file
def get_filename():
    file_name = filedialog.askopenfilename()
    initialdir="/",
    title="Select file",
    filetypes=(("jpeg", "*.jpg"), ("PNG", "*.png"), ("all files", "*.*"))
    if not file_name:    # user canceled
        log.logger.info("User canceled open dialog")
    else:
        return file_name


def set_filename():
    file_name = dialogs.filename = filedialog.logger.asksaveasfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("jpeg", "*.jpg"), ("PNG", "*.png"), ("all files", "*.*")),
        )
    if not file_name:    # user canceled
        log.logger.info("User canceled save dialog")
    else:
        return file_name


# returns the API or secret key
def get_key(key_type, file_name):
    if not os.path.exists(file_name):
        print("File not found")
        log.logger.error("API key file not found")
    with open(file_name, 'r') as read_file:
        keys = json.load(read_file)

    return keys[key_type]

