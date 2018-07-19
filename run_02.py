# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task
import itertools
import logging
import socket
from logging.handlers import RotatingFileHandler

from business.approve import LaunchApproval, WaitApproval


'''
# 审批(发起的审批)

# 审批(待我审批)

'''


def append_file_logger():
    root_logger = logging.getLogger()
    log_format = "%(asctime)s.%(msecs)03d000 [%(levelname)s] {0}/%(name)s : %(message)s".format(socket.gethostname())
    formatter = logging.Formatter(log_format, '%Y-%m-%d %H:%M:%S')
    file_handler = RotatingFileHandler('./locust_02.log', maxBytes=5 * 1024 * 1024, backupCount=3)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)     

append_file_logger()

counter = itertools.count()

class UserBehavior(TaskSet):
    
    def on_start(self):
        self.logger = logging.getLogger('locust-%03d'% counter.__next__())
        self.logger.info('Hatching locust-logger')
            
        
    tasks = {LaunchApproval:10, WaitApproval:10}
    
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000