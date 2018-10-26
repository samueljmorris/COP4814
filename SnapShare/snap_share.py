from flickr_helper import FlickrHelper
import custom_logs as cl
log = cl.CLog(module=__name__, file="SnapShare.log")

log.logger.info("Main started")
flickr = FlickrHelper("parsed-json")


# Usage examples:
# flickr.download("44648763065")
# flickr.upload()
# flickr.download("44648763065")
# flickr.photo_info("44648763065")
# flickr.get_sizes("44648763065")
# flickr.get_context("44648763065")


