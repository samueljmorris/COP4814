import json
import flickrapi
import shutil
from util import *
import custom_logs as cl
import os
import requests
log = cl.CLog(module="main", file="SnapShare.log")
log.logger.info("Application started")


# initializes a session object with anonymous user
def initialize_api():
    sec_key = get_key("flickr_secret")
    api_key = get_key("flickr_key")
    global flickr
    flickr = flickrapi.FlickrAPI(api_key, sec_key, format="parsed-json")
    flickr.authenticate_via_browser(perms="read")
    log.logger.info("API Initialized")


# returns info for a specified photo_id
def photo_info(pid_in):
    return flickr.photos.getInfo(photo_id=pid_in)


# returns the previous and next photos in a photo stream
def get_context(pid_in):
    return flickr.photos.getContext(photo_id=pid_in)


# returns the available sizes for the photo. **Also provides direct URL**
def get_sizes(pid_in):
    return flickr.photos.getSizes(photo_id=pid_in)


# uploads a photo
def upload_photo():
    f_name = get_filename()
    photo_id = flickr.photos.uploadPhoto(f_name)
    return photo_id


# download photo with photo ID pid_in
def download_photo(pid_in, size):
    size_info = get_sizes(pid_in)
    for key in size_info["sizes"]["size"]:
        if key["label"] == size:
            url = key["source"]

    # prompt the user for a filename and write the binary data returned by server to specified file
    # TODO: figure out how to pre-populate the save as dialog with the filename
    file = set_filename()
    if file:
        response = requests.get(url, stream=True)
        with open(file, 'wb') as output:
            shutil.copyfileobj(response.raw, output)
    else:
        log.logger.error("No filename provided to download_photo function")

    print(url)


initialize_api()
download_photo("5457365307", "Original")




