# -*- coding:utf-8 -*-

import time, itertools
from locust import HttpLocust, TaskSet
from common import log
from locustfiles.list import ListTask


class UserBehavior(TaskSet):
    
        
    def on_start(self):
        counter = itertools.count(1)
        log_name_format = time.strftime("_%Y%m%d%H%M%S", time.localtime()) + '.log'
        log_path = __file__.replace('.py', log_name_format)
        log.append_file_logger(self, log_path, counter)
        
    #tasks = {Contract: 10, Project: 10, Task: 10}
    tasks = {ListTask}
    
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000