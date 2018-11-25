# -*- coding:utf-8 -*-

from locust import HttpLocust, TaskSet
from locustfiles.list import ListTask


class UserBehavior(TaskSet):    
    
    tasks = {ListTask}
    
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000