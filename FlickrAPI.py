import json
import requests


# returns the API or secret key
def get_key(key_type):

    with open("flickr_api_key.json", 'r') as read_file:
        api_key = json.load(read_file)

    flickr_api_key = api_key[key_type]
    return flickr_api_key


# updates specified file with JSON data
def update_file(data, file_name):

    with open(file_name, 'a') as file:
        json.dump(data, file, indent=4)


# overwrites specified file with JSON data
def overwrite_file(data, file_name):

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


# returns info about photo with ID photo_id
def get_info(photo_id):
    url_comps = {"method_url": "flickr.photos.getInfo", "photo_id_url": photo_id}
    return requests.get(generate_url(url_comps)).json()


def get_all_contexts(photo_id):
    url_comps = {"method_url": "flickr.photos.getAllContexts", "photo_id_url": photo_id}
    return requests.get(generate_url(url_comps)).json()


def get_context(photo_id):
    url_comps = {"method_url": "flickr.photos.getContext", "photo_id_url": photo_id}
    return requests.get(generate_url(url_comps)).json()


# generates url for the API call
def generate_url(url_comps):

    key = get_key("flickr_key")

    url_comps["photo_id_url"] = "&photo_id=" + url_comps.get("photo_id_url")
    url_comps["format_url"] = "&format=json&nojsoncallback=1"
    # auth_token_url = "&auth_token="
    # api_sig_url = "&api_sig="

    url = "https://api.flickr.com/services/rest/" + "?method=" + url_comps.get("method_url") + "&api_key=" + key

    for key, value in url_comps.items():
        if key != "method_url":
            url = url + value

    url + url_comps["format_url"]

    return url



