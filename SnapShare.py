import json
import requests
import flickrapi


# returns the API or secret key
def get_key(key_type):

    with open("flickr_api_key.json", 'r') as read_file:
        api_key = json.load(read_file)

    flickr_api_key = api_key[key_type]
    return flickr_api_key


# initializes a flickr object with API key
def initialize_api():
    global flickr
    sec_key = get_key("flickr_secret")
    api_key = get_key("flickr_key")
    flickr = flickrapi.FlickrAPI(api_key, sec_key, format='parsed-json')


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


def authenticate_read_only():
    flickr.authenticate_via_browser(perms='read')


def authenticate_write_perms():
    flickr.authenticate_via_browser(perms='write')


initialize_api()
print(flickr.photos.getInfo(photo_id='43593563660'))
print(photo_info('43593563660'))
