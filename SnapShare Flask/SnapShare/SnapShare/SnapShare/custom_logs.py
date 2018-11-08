import logging


# initialize log location and format
class CLog:

    def __init__(self, **kwargs):

                # set module name if passed as paramater, otherwise "NA"
                if "module" in kwargs:
                    self.logger = logging.getLogger(kwargs["module"])
                else:
                    self.logger = logging.getLogger("N/A")

                if "file" in kwargs:
                    self.file = kwargs["file"]
                else:
                    self.file = "log.txt"

                self.logger.setLevel("INFO")
                self.log_handler = logging.FileHandler(self.file)
                self.formatter = logging.Formatter("%(levelname)s  |  %(asctime)s  |  %(name)s  |  %(message)s")
                self.log_handler.setFormatter(self.formatter)
                self.logger.addHandler(self.log_handler)



