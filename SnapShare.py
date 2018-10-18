import json
import requests
import flickrapi
import tkinter
from tkinter import filedialog


# returns the API or secret key
def get_key(key_type):

    with open("flickr_api_key.json", 'r') as read_file:
        api_key = json.load(read_file)

    flickr_api_key = api_key[key_type]
    return flickr_api_key


# initializes a flickr object with anonymous user
def initialize_api_anon():
    global flickr
    sec_key = get_key("flickr_secret")
    api_key = get_key("flickr_key")
    flickr = flickrapi.FlickrAPI(api_key, sec_key, format='parsed-json')


# initializes a flickr object with logged in user
def initialize_api_user(user_token):
    sec_key = get_key("flickr_secret")
    api_key = get_key("flickr_key")
    flickr = flickrapi.FlickrAPI(api_key, sec_key, format='parsed-json', token=user_token)


# returns info for a specified photo_id
def photo_info(photo_id_in):
    return flickr.photos.getInfo(photo_id=photo_id_in)


# updates specified file with JSON data
def update_file(data, file_name):

    with open(file_name, 'a') as file:
        json.dump(data, file, indent=4)


# overwrites specified file with JSON data
def overwrite_file(data, file_name):

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


# generates a user token with read only permissions
def authenticate_read_only():
    flickr.authenticate_via_browser(perms='read')


# generates a user token with write permissions
def authenticate_write_perms():
    flickr.authenticate_via_browser(perms='write')


# checks if the user token is valid
def check_token():
    return flickr.token_valid()


# uploads a photo
def upload_photo(file_name):
    return file_name


def get_filename():
    root = Tk()
    root.filename = filedialog.askopenfilename()

upload_photo(get_filename())

