import logging
import time, itertools
from logging.handlers import RotatingFileHandler
import socket

'''
had been abandoned, because already having the --logfile option
'''


def append_file_logger(self, log_path):
    root_logger = logging.getLogger()
    log_format = "%(asctime)s.%(msecs)03d000 [%(levelname)s] {0}/%(name)s : %(message)s".format(socket.gethostname())
    formatter = logging.Formatter(log_format, '%Y-%m-%d %H:%M:%S')
    file_handler = RotatingFileHandler(log_path, maxBytes=5 * 1024 * 1024, backupCount=3)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)


try:
    if isinstance(counter, object):
        pass
except:
    counter = itertools.count(1)
    log_name_format = time.strftime("_%Y%m%d%H%M%S", time.localtime()) + '.log'
    log_path = __file__.replace('.py', log_name_format)
    log.append_file_logger(self, log_path)

self.logger = logging.getLogger('%s-%03d'% ("all_run", counter.__next__()))
self.logger.info('Hatching locust-logger(all_run)')     