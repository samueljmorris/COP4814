from flickr_helper import FlickrHelper
import custom_logs as cl
import xml.etree.ElementTree as Et

log = cl.CLog(module=__name__, file="SnapShare.log")
log.logger.info("Main started")
flickr_rest = FlickrHelper("rest")
flickr_parsed = FlickrHelper("parsed-json")

root = Et.fromstring(flickr_rest.upload())
pid = root[0].text
print(pid)


flickr_parsed.download("44648763065")
# flickr.download("44648763065")
# flickr.upload()
# flickr.download("44648763065")
# flickr.photo_info("44648763065")
# flickr.get_sizes("44648763065")
# flickr.get_context("44648763065")


