import flickrapi
import shutil
from util import *
import custom_logs as cl
import requests
log = cl.CLog(module="main", file="SnapShare.log")
log.logger.info("Application started")


# initializes an API helper object with raw JSON as response format
def init_api_json():
    sec_key = get_key("flickr_secret")
    api_key = get_key("flickr_key")
    global flickr
    flickr = flickrapi.FlickrAPI(api_key, sec_key, format="json", store_token="false")
    flickr.authenticate_via_browser(perms="write")
    log.logger.info("API Initialized with JSON")


# initializes an API helper object with parsed JSON as response format
def init_api_parsed():
    sec_key = get_key("flickr_secret")
    api_key = get_key("flickr_key")
    global flickr
    flickr = flickrapi.FlickrAPI(api_key, sec_key, format="parsed-json", store_token=True)
    flickr.authenticate_via_browser(perms="write")
    log.logger.info("API Initialized with parsed JSON")


# initializes an API helper object with parsed REST as response format
def init_api_rest():
    sec_key = get_key("flickr_secret")
    api_key = get_key("flickr_key")
    global flickr
    flickr = flickrapi.FlickrAPI(api_key, sec_key, format="rest", store_token=True)
    flickr.authenticate_via_browser(perms="write")
    log.logger.info("API Initialized with XML")


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
def upload_photo(**kwargs):
    init_api_rest()
    file = get_filename()
    params = {"filename=": file}

    # TODO: Convert kwargs to string to pass optional parameters
    if "tags" in kwargs:
        for key, value in kwargs["tags"]:
            tags = tags + value + " "
        params["tags"] = tags
    log.logger.info("Attempting to upload file")
    flickr.upload(filename=file)


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


upload_photo()


