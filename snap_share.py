import json
import flickrapi
from util import *
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# initialize log location and format
log_handler = logging.FileHandler('SnapShare.log')
formatter = logging.Formatter('%(levelname)s  |  %(asctime)s  |  %(name)s  |  %(message)s')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

logger.info("Application started")


# initializes a session object with anonymous user
def initialize_api():
    sec_key = get_key("flickr_secret")
    api_key = get_key("flickr_key")
    flickr = flickrapi.FlickrAPI(api_key, sec_key, format='parsed-json')
    flickr.authenticate_via_browser(perms='read')
    logger.info("API Initialized")


# returns info for a specified photo_id
def photo_info(pid_in):
    return flickr_api.photos.getInfo(photo_id=pid_in)


# uploads a photo
def upload_photo():
    f_name = get_filename()
    photo_id = flickr_api.photos.uploadPhoto(f_name)
    return photo_id


# returns the previous and next photos in a photo stream
def get_context(photo_id):
    return flickr_api.photos.getContext(photo_id=photo_id)







