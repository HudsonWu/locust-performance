# -*- coding: utf-8 -*-

from locust import TaskSet, task

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijg1NTE4MWJhNTcwY2VkNzg2MDM3YTFkMjk3YzIwOWY4ZjQxNWRjNGVlMGM2N2M3MDJhN2U2NTA0Y2JiMDAxZDg4YzRiMGVmZGU1MzM2ZWU3In0.eyJhdWQiOiIyIiwianRpIjoiODU1MTgxYmE1NzBjZWQ3ODYwMzdhMWQyOTdjMjA5ZjhmNDE1ZGM0ZWUwYzY3YzcwMmE3ZTY1MDRjYmIwMDFkODhjNGIwZWZkZTUzMzZlZTciLCJpYXQiOjE1MzE3MTA2NTYsIm5iZiI6MTUzMTcxMDY1NiwiZXhwIjoxODQ3MDcwNjU2LCJzdWIiOiIzMSIsInNjb3BlcyI6W119.HUKpyEhcIuIwdzYqHI_fxH6M62NnMlaDnCel289YmH6NxKVjtgTOuqJnXQHG-hG3Hx61ix2vg4LbQI6VkXndvb7Rotdr04CWcPuwCGq2mkJEelCpc-X5pqRNsE7opoKk3saLdc1VK4tl33NPrVb1PdvMajMdq6rMWBOxQ07IqyEXRd9D-KKBb1NuDnHVW2YfhgnmjRkQu_ebZ8vBY-_VspePX252tqjmIJpJto2Mp2jRf_F-2lD0vt6UdFr6Lbz8-yJ9WhluocCigMa9p07XBT8Eh5u4CMrgAYe7szmnkow49r-0wduNiNxHCeMfEa5g7w7X_94e7rKjqJbjlSamxzH44jRLzC2PN59D4VfsBP9yw8ZdhMxs-DMaMh1hIjINLd7WfFE9NkNc5NWrApf3osAmVEUgRRknuq62wHyJYFtPdJMAhwxzTByHOMmTrNOWY5pDyyMvDp-Svf0BDkcZMKO9FnpU6xnkIoy0UC74b4GjgUvSgdj_CCmpNPoTYPx1yNR0Zg_ycDRt0uKlHXWyX4OWNvyeRua75ORHGyn8-j0mz2-qNxzbAnPholQx9r1vIVEVPwj7CnLTU_yRCxqvSA4K8HvFex6DyfIHA2fqw2gh6aa4ozz_NymsK38aSVN1Bdr-H3ow4kWJOTx5Nt5hCWqNWkI6Nw_3icPaXQxboqI"
headers = {'Accept': 'application/json', 'Authorization': 'Bearer '+str(access_token)}
consulting_id = "o803wk5py54mg6dl"

class MyContract(TaskSet):
       
    @task(10)
    def all_mycontracts(self):
        self.client.get(name=u'我的合同-全部', url="/v1/my/contracts?limit=10&page=1&consulting_id=%s"% consulting_id,\
                        headers=headers)
    
    @task(8)
    def seal_mycontracts(self):
        self.client.get(name=u'我的合同-盖章', url="/v1/my/contracts?limit=10&page=1&contract_status=3&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def back_mycontracts(self):
        self.client.get(name=u'我的合同-已回', url="/v1/my/contracts?limit=10&page=1&contract_status=2&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def invalid_mycontracts(self):
        self.client.get(name=u'我的合同-作废', url="/v1/my/contracts?limit=10&page=1&contract_status=4&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def special_mycontracts(self):
        self.client.get(name=u'我的合同-特批', url="/v1/my/contracts?limit=10&page=1&contract_status=5&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def complete_mycontracts(self):
        self.client.get(name=u'我的合同-完成', url="/v1/my/contracts?limit=10&page=1&contract_status=6&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def search_mycontracts(self):
        self.client.get(name=u'我的合同-搜索', url=u"/v1/my/contracts?limit=10&page=1&search=项目&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(5)
    def stop(self):
        self.interrupt()


class AllContract(TaskSet):
       
    @task(10)
    def all_contracts(self):
        self.client.get(name=u'所有合同-全部', url="/v1/self/contracts?limit=10&page=1&consulting_id=%s"% consulting_id,\
                        headers=headers)
    
    @task(8)
    def seal_contracts(self):
        self.client.get(name=u'所有合同-盖章', url="/v1/self/contracts?limit=10&page=1&contract_status=3&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def back_contracts(self):
        self.client.get(name=u'所有合同-已回', url="/v1/self/contracts?limit=10&page=1&contract_status=2&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def invalid_contracts(self):
        self.client.get(name=u'所有合同-作废', url="/v1/self/contracts?limit=10&page=1&contract_status=4&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def special_contracts(self):
        self.client.get(name=u'所有合同-特批', url="/v1/self/contracts?limit=10&page=1&contract_status=5&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def complete_contracts(self):
        self.client.get(name=u'所有合同-完成', url="/v1/self/contracts?limit=10&page=1&contract_status=6&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def search_contracts(self):
        self.client.get(name=u'所有合同-搜索', url=u"/v1/self/contracts?limit=10&page=1&search=项目&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(5)
    def stop(self):
        self.interrupt()