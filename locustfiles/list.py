# -*- coding: utf-8 -*-

import sys
from os.path import pardir, sep
sys.path.append(pardir + sep)
import time, itertools
from locust import HttpLocust, TaskSet
from common import log
from business.contract import Contract
from business.project import Project
from business.task import Taskb
from business.approval import Approval



'''
合同、项目、任务的列表请求

变量保持不变：
1. 数据库表数据保持一致
contracts、projects、tasks表数据条数保持一致(设置成1000条)
2. 接口请求后返回的数据等于10条(limit=10&page=1)
'''


class ListTask(TaskSet):
        
    def on_start(self):
        
        try:
            if isinstance(counter_list, object):
                pass
        except:
            counter_list = itertools.count(1)

        log_name_format = time.strftime("_%Y%m%d%H%M%S", time.localtime()) + '.log'
        log_path = __file__.replace('.py', log_name_format)
        log.append_file_logger(self, log_path, "list", counter_list)
        
    tasks = {Contract: 10, Project: 10, Taskb: 10, Approval: 10}
    
    def stop(self):
        self.interrupt()


class ListUser(HttpLocust):
    task_set = ListTask
    min_wait = 5000
    max_wait = 10000