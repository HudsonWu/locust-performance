# -*- coding: utf-8 -*-

from locust import TaskSet, task

# 认证信息
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImM4ZDk4NWUzOTEyNDkzMWI1NTBhY2I2MTE1YTZjMjQxZDlhOWM4Zjk4NDZmYjFhNjRiYWEwM2MwZjMxOGJmYTBmYzY4MjBkNzYyZWFhNjRkIn0.eyJhdWQiOiIyIiwianRpIjoiYzhkOTg1ZTM5MTI0OTMxYjU1MGFjYjYxMTVhNmMyNDFkOWE5YzhmOTg0NmZiMWE2NGJhYTAzYzBmMzE4YmZhMGZjNjgyMGQ3NjJlYWE2NGQiLCJpYXQiOjE1MzE5NjM4NjQsIm5iZiI6MTUzMTk2Mzg2NCwiZXhwIjoxODQ3MzIzODY0LCJzdWIiOiIzNyIsInNjb3BlcyI6W119.iOPJVrKoYqTs55_1rS_OAU5ZlDjoVrvzuBgtY-3QjMKmUARoUOJKuKdgnE1Cmq4gj2jlBi2cuPfStRZEMlEwM7TuCU4PXYSYD4wb5hDDFqvrdgvkc6kPA3cq5bemJKQC6CeTP3PmCQ_ILyATPZAOMsMzThAvh-FCLns5W_82hNG1bn-g410KGAbH_YgiqW6VNzNE0wom4DK7niqsiL8T31mV_-FG2P7r0-lejEXEViOWhAn1zcNmEpMFjPrijfmsfH50BA0WPXP9T3SYxEYlOnD-0zP13RIx4w4NHKOpho-w4udIFmlUBL2TR0CRhN8QeY2zmqGN8uKx7rRyDBiUV-lM3BaQK3L4LAYZQ_lkgTcXnCFlYjN5rZSVxnkUUFMyW4VHUzMVK3VEzTRuYaBQb4nbxYz7zFQPVjg1BRhAVyHmRIi4mnCwMPfiRGXOQxcTfJVZKOW4bFL68Dqp6hzmkdT-iDBzPlxIScXR1tLTUgKA8XMvNHUYZbkgO1E-XHkD2Oc35HxmTC1oP1K_FR_TsNSTy-wKiKXYJ1u5OMU6o8ZAMwnxWs-3q94TC0swh--ktW9GXr_HUIIlSTeE_tBUTkV0vcLFfwTlg789ncVbr-CuP1hTCU27sleacn8SoIx9rLqkobtodTB7Hc2EaHBRL--dRDPcHfDYUQfmbG_9iQM"
consulting_id = "omx8kwrgl5aep3nv"

headers = {'Accept': 'application/json', 'Authorization': 'Bearer '+str(access_token)}


class MyContract(TaskSet):
       
    @task(10)
    def all_mycontracts(self):
        self.client.get(name=u'我的合同-全部', headers=headers, \
                        url="/v1/my/contracts?limit=10&page=1&consulting_id=%s"% consulting_id)
    
    @task(8)
    def seal_mycontracts(self):
        self.client.get(name=u'我的合同-盖章', headers=headers, \
                        url="/v1/my/contracts?limit=10&page=1&contract_status=3&consulting_id=%s"% consulting_id)
        
    @task(8)
    def back_mycontracts(self):
        self.client.get(name=u'我的合同-已回', headers=headers, \
                        url="/v1/my/contracts?limit=10&page=1&contract_status=2&consulting_id=%s"% consulting_id)
        
    @task(8)
    def invalid_mycontracts(self):
        self.client.get(name=u'我的合同-作废', headers=headers, \
                        url="/v1/my/contracts?limit=10&page=1&contract_status=4&consulting_id=%s"% consulting_id)
        
    @task(8)
    def special_mycontracts(self):
        self.client.get(name=u'我的合同-特批', headers=headers, \
                        url="/v1/my/contracts?limit=10&page=1&contract_status=5&consulting_id=%s"% consulting_id)
        
    @task(8)
    def complete_mycontracts(self):
        self.client.get(name=u'我的合同-完成', headers=headers, \
                        url="/v1/my/contracts?limit=10&page=1&contract_status=6&consulting_id=%s"% consulting_id)
        
    @task(8)
    def search_mycontracts(self):
        self.client.get(name=u'我的合同-搜索', url=u"/v1/my/contracts?limit=10&page=1&search=项目&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(10)
    def stop(self):
        self.interrupt()


class AllContract(TaskSet):
       
    @task(10)
    def all_contracts(self):
        self.client.get(name=u'所有合同-全部', headers=headers, \
                        url="/v1/self/contracts?limit=10&page=1&consulting_id=%s"% consulting_id)
    
    @task(8)
    def seal_contracts(self):
        self.client.get(name=u'所有合同-盖章', headers=headers, \
                        url="/v1/self/contracts?limit=10&page=1&contract_status=3&consulting_id=%s"% consulting_id)
        
    @task(8)
    def back_contracts(self):
        self.client.get(name=u'所有合同-已回', headers=headers, \
                        url="/v1/self/contracts?limit=10&page=1&contract_status=2&consulting_id=%s"% consulting_id)
        
    @task(8)
    def invalid_contracts(self):
        self.client.get(name=u'所有合同-作废', headers=headers, \
                        url="/v1/self/contracts?limit=10&page=1&contract_status=4&consulting_id=%s"% consulting_id)
        
    @task(8)
    def special_contracts(self):
        self.client.get(name=u'所有合同-特批', headers=headers, \
                        url="/v1/self/contracts?limit=10&page=1&contract_status=5&consulting_id=%s"% consulting_id)
        
    @task(8)
    def complete_contracts(self):
        self.client.get(name=u'所有合同-完成', headers=headers, \
                        url="/v1/self/contracts?limit=10&page=1&contract_status=6&consulting_id=%s"% consulting_id)
        
    @task(8)
    def search_contracts(self):
        self.client.get(name=u'所有合同-搜索', headers=headers, \
                        url=u"/v1/self/contracts?limit=10&page=1&search=项目&consulting_id=%s"% consulting_id)
        
    @task(5)
    def stop(self):
        self.interrupt()