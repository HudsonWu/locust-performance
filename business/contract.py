# -*- coding: utf-8 -*-

from locust import TaskSet, task, seq_task
from common import config


#合同管理

#不同权限, 获取合同列表
class ContractPriv(TaskSet):
       
    @task(10)
    def all_mycontracts(self):
        self.client.get(name=u'我的合同-全部', headers=config.headers, \
                        url="/v1/my/contracts?limit=10&page=1&consulting_id=%s"% config.consulting_id)
    
    @task(10)
    def all_contracts(self):
        self.client.get(name=u'所有合同-全部', headers=config.headers, \
                        url="/v1/self/contracts?limit=10&page=1&consulting_id=%s"% config.consulting_id)
    
    @task
    def stop(self):
        self.interrupt()

#根据合同状态进行切换
class ContractStatus(TaskSet):
        
    @task(8)
    def seal_mycontracts(self):
        self.client.get(name=u'我的合同-盖章', headers=config.headers, \
                        url="/v1/my/contracts?limit=10&page=1&contract_status=3&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def back_mycontracts(self):
        self.client.get(name=u'我的合同-已回', headers=config.headers, \
                        url="/v1/my/contracts?limit=10&page=1&contract_status=2&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def invalid_mycontracts(self):
        self.client.get(name=u'我的合同-作废', headers=config.headers, \
                        url="/v1/my/contracts?limit=10&page=1&contract_status=4&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def special_mycontracts(self):
        self.client.get(name=u'我的合同-特批', headers=config.headers, \
                        url="/v1/my/contracts?limit=10&page=1&contract_status=5&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def complete_mycontracts(self):
        self.client.get(name=u'我的合同-完成', headers=config.headers, \
                        url="/v1/my/contracts?limit=10&page=1&contract_status=6&consulting_id=%s"% config.consulting_id)
        
    
    @task(8)
    def seal_contracts(self):
        self.client.get(name=u'所有合同-盖章', headers=config.headers, \
                        url="/v1/self/contracts?limit=10&page=1&contract_status=3&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def back_contracts(self):
        self.client.get(name=u'所有合同-已回', headers=config.headers, \
                        url="/v1/self/contracts?limit=10&page=1&contract_status=2&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def invalid_contracts(self):
        self.client.get(name=u'所有合同-作废', headers=config.headers, \
                        url="/v1/self/contracts?limit=10&page=1&contract_status=4&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def special_contracts(self):
        self.client.get(name=u'所有合同-特批', headers=config.headers, \
                        url="/v1/self/contracts?limit=10&page=1&contract_status=5&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def complete_contracts(self):
        self.client.get(name=u'所有合同-完成', headers=config.headers, \
                        url="/v1/self/contracts?limit=10&page=1&contract_status=6&consulting_id=%s"% config.consulting_id)
    
    @task
    def stop(self):
        self.interrupt()    
        

# web端合同筛选功能
class ContractFilter(TaskSet):
    
    @task(8)
    def search_contracts(self):
        self.client.get(name=u'所有合同-搜索', headers=config.headers, \
                        url=u"/v1/self/contracts?limit=10&page=1&search=项目&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def search_mycontracts(self):
        self.client.get(name=u'我的合同-搜索', url=u"/v1/my/contracts?limit=10&page=1&search=项目&consulting_id=%s"% config.consulting_id,\
                        headers    =config.headers)
    
    @task
    def stop(self):
        self.interrupt()    


class Contract(TaskSet):
    
    tasks = {ContractPriv: 10, ContractStatus: 10, ContractFilter: 10}
    
    @task
    def stop(self):
        self.interrupt()