# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task
import itertools
import logging
import socket
from logging.handlers import RotatingFileHandler
from business.contract import MyContract, AllContract
from business.project import MyProject, AllProject, ManageProject
from business.task import ReceiveTask, SendTask



def append_file_logger():
    root_logger = logging.getLogger()
    log_format = "%(asctime)s.%(msecs)03d000 [%(levelname)s] {0}/%(name)s : %(message)s".format(socket.gethostname())
    formatter = logging.Formatter(log_format, '%Y-%m-%d %H:%M:%S')
    file_handler = RotatingFileHandler('./locust.log', maxBytes=5 * 1024 * 1024, backupCount=3)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)     

append_file_logger()

counter = itertools.count()

'''
def get_token(self):
    post_data = dict(username='test029@zwehs.com', password='123456')
    with self.client.post(name='login', url="/v1/client/login",\
                                data=post_data) as response:
        data = response.json()
        access_token = data['access_token']
        headers = {'Accept':'application/json',\
               'Authorization':'Bearer '+str(access_token)}
        print("status_code: %s\naccess_token: %s"% (response.status_code, access_token))

def get_console(self):
    
    #获取我的控制台
    #返回当前账户的角色信息
    
    print(headers)
    with self.client.get(name='console', url="/v1/web/my/console",\
                         headers=headers) as response:
        print("status_code: %s"% response.status_code)
        data = response.json()
        roles = data['data']
        for i in roles:
            if roles[i]['identity'] == "consulting":
                consulting_id = roles[i]['identity_id']
                consulting_name = roles[i]['name']
                print("consulting_name: %s"% consulting_name)
                break
            i = i + 1
        if consulting_id == "":
            print(u'当前账户不存在咨询机构角色!!!')
            exit(0)
'''
    

class UserBehavior(TaskSet):
    
    def on_start(self):
        self.logger = logging.getLogger('locust-%03d'% counter.__next__())
        self.logger.info('Hatching locust-logger')
        
        #get_token(self)
        #get_console(self)    
        
    tasks = {MyContract:20, AllContract:10, MyProject:20, AllProject:10, ManageProject:10, ReceiveTask:10, SendTask:10}
    
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000
