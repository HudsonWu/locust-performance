# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task
import queue

class UserBehavior(TaskSet):
    
    @task
    def test_login(self):
        '''
        所有并发虚拟用户共享同一份测试数据，保证用户使用的数据不重复，
        并且数据可循环使用
        '''
        try:
            data = self.locust.user_data_queue.get()
        except queue.Empty:
            print(u'队列中没有账户了，用户登录测试结束')
            exit(0)
        
        print(u'登录账号: {}'\
              .format(data['username']))
        payload = {
            'username': data['username'],
            'password': data['password']
        }
        self.client.post('/v1/client/login', data=payload)
        self.locust.user_data_queue.put_nowait(data)     
   
class WebsiteUser(HttpLocust):
    host = 'http://dev.api.zwehs.com'
    task_set = UserBehavior
    
    user_data_queue = queue.Queue()
    for index in range(1, 11):
        data = {
            "username": "test%03d@zwehs.com" % index,
            "password": "123456"
        }
        user_data_queue.put_nowait(data)
        
    min_wait = 5000
    max_wait = 10000
