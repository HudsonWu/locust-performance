import logging
from logging.handlers import RotatingFileHandler
import itertools
import socket

counter = itertools.count()

def append_file_logger(self, log_path):
    root_logger = logging.getLogger()
    log_format = "%(asctime)s.%(msecs)03d000 [%(levelname)s] {0}/%(name)s : %(message)s".format(socket.gethostname())
    formatter = logging.Formatter(log_format, '%Y-%m-%d %H:%M:%S')
    file_handler = RotatingFileHandler(log_path, maxBytes=5 * 1024 * 1024, backupCount=3)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)

    self.logger = logging.getLogger('locust-%03d'% counter.__next__())
    self.logger.info('Hatching locust-logger')