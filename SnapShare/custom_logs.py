import logging


class CLog:

    def __init__(self, file, module):

                # initialize log location and format
                self.logger = logging.getLogger(module)
                self.file = file
                logging.basicConfig(level=logging.INFO)
                self.log_handler = logging.FileHandler(file)
                self.formatter = logging.Formatter("%(levelname)s  |  %(asctime)s  |  %(name)s  |  %(message)s")
                self.log_handler.setFormatter(self.formatter)
                self.logger.addHandler(self.log_handler)


