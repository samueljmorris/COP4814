import flickrapi
import shutil
from util import *
import requests
import custom_logs as cl
log = cl.CLog(module=__name__, file="SnapShare.log")
supported_formats = {"json", "parsed-json", "rest"}


class FlickrHelper:

            def __init__(self, *args):
                api_key = get_key("flickr_key", "flickr_api_key.json")
                sec_key = get_key("flickr_secret", "flickr_api_key.json")

                if args:
                    self.format = args[0]
                    if self.format not in supported_formats:
                        log.logger.error("Unsupported format provided, defaulting to parsed-json")
                        self.flickr = flickrapi.FlickrAPI(api_key, sec_key)

                    self.flickr = flickrapi.FlickrAPI(api_key, sec_key, format=self.format)
                    log.logger.info("API Initialized with " + self.format)
                else:
                    self.flickr = flickrapi.FlickrAPI(api_key, sec_key, format="parsed-json")
                    log.logger.info("API Initialized with default format")

                self.flickr.authenticate_via_browser(perms="write")

            # returns info for a specified photo_id
            def photo_info(self, pid_in):
                return self.flickr.photos.getInfo(photo_id=pid_in)

            # returns the previous and next photos in a photo stream
            def get_context(self, pid_in):
                return self.flickr.photos.getContext(photo_id=pid_in)

            # returns the available sizes for the photo. **Also provides direct URL**
            def get_sizes(self, pid_in):
                return self.flickr.photos.getSizes(photo_id=pid_in)

            # uploads a photo
            def upload(self, **kwargs):
                file = get_filename()
                params = {"filename=": file}

                # TODO: Convert kwargs to string to pass optional parameters
                if "tags" in kwargs:
                    for key, value in kwargs["tags"]:
                        tags = tags + value + " "
                    params["tags"] = tags

                log.logger.info("Attempting to upload file")
                self.flickr.upload(filename=file)

            # download photo with photo ID pid_in
            def download(self, pid_in, *args):

                # get available sizes for photo at pid_in
                size_info = self.get_sizes(pid_in)
                url = ""

                # check if a size is passed as parameter
                if args:

                    # check if size is available and default to "Original" if not or if no parameter
                    for key in size_info["sizes"]["size"]:
                        if key["label"] == args[0]:
                            url = key["source"]

                if url == "":

                    for key in size_info["sizes"]["size"]:
                        if key["label"] == "Original":
                            url = key["source"]

                log.logger.info("Download function determined url = " + url)

                # prompt the user for a filename and write the binary data returned by server to specified file
                # TODO: figure out how to pre-populate the save as dialog with the filename
                file = set_filename()
                if file:
                    response = requests.get(url, stream=True)
                    with open(file, 'wb') as output:
                        shutil.copyfileobj(response.raw, output)
                else:
                    log.logger.error("No filename provided to download_photo function")
