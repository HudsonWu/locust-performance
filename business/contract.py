# -*- coding: utf-8 -*-

from locust import TaskSet, task

# 测试服务器
# access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijg1NTE4MWJhNTcwY2VkNzg2MDM3YTFkMjk3YzIwOWY4ZjQxNWRjNGVlMGM2N2M3MDJhN2U2NTA0Y2JiMDAxZDg4YzRiMGVmZGU1MzM2ZWU3In0.eyJhdWQiOiIyIiwianRpIjoiODU1MTgxYmE1NzBjZWQ3ODYwMzdhMWQyOTdjMjA5ZjhmNDE1ZGM0ZWUwYzY3YzcwMmE3ZTY1MDRjYmIwMDFkODhjNGIwZWZkZTUzMzZlZTciLCJpYXQiOjE1MzE3MTA2NTYsIm5iZiI6MTUzMTcxMDY1NiwiZXhwIjoxODQ3MDcwNjU2LCJzdWIiOiIzMSIsInNjb3BlcyI6W119.HUKpyEhcIuIwdzYqHI_fxH6M62NnMlaDnCel289YmH6NxKVjtgTOuqJnXQHG-hG3Hx61ix2vg4LbQI6VkXndvb7Rotdr04CWcPuwCGq2mkJEelCpc-X5pqRNsE7opoKk3saLdc1VK4tl33NPrVb1PdvMajMdq6rMWBOxQ07IqyEXRd9D-KKBb1NuDnHVW2YfhgnmjRkQu_ebZ8vBY-_VspePX252tqjmIJpJto2Mp2jRf_F-2lD0vt6UdFr6Lbz8-yJ9WhluocCigMa9p07XBT8Eh5u4CMrgAYe7szmnkow49r-0wduNiNxHCeMfEa5g7w7X_94e7rKjqJbjlSamxzH44jRLzC2PN59D4VfsBP9yw8ZdhMxs-DMaMh1hIjINLd7WfFE9NkNc5NWrApf3osAmVEUgRRknuq62wHyJYFtPdJMAhwxzTByHOMmTrNOWY5pDyyMvDp-Svf0BDkcZMKO9FnpU6xnkIoy0UC74b4GjgUvSgdj_CCmpNPoTYPx1yNR0Zg_ycDRt0uKlHXWyX4OWNvyeRua75ORHGyn8-j0mz2-qNxzbAnPholQx9r1vIVEVPwj7CnLTU_yRCxqvSA4K8HvFex6DyfIHA2fqw2gh6aa4ozz_NymsK38aSVN1Bdr-H3ow4kWJOTx5Nt5hCWqNWkI6Nw_3icPaXQxboqI"
# consulting_id = "o803wk5py54mg6dl"

# 线上服务器
access_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImY4ODI1YjllZDU2ZDc1NDU2Y2JhYTcyNjI3NWNlMmQzZTZhYmM5ODRhMThiOWM3NzU0OWZhOGYzYTdlOGQ5YmMyMjJkZDUxZTFkMTdmMDI2In0.eyJhdWQiOiIyIiwianRpIjoiZjg4MjViOWVkNTZkNzU0NTZjYmFhNzI2Mjc1Y2UyZDNlNmFiYzk4NGExOGI5Yzc3NTQ5ZmE4ZjNhN2U4ZDliYzIyMmRkNTFlMWQxN2YwMjYiLCJpYXQiOjE1MzE3MTEwNDUsIm5iZiI6MTUzMTcxMTA0NSwiZXhwIjoxODQ3MDcxMDQ1LCJzdWIiOiIzNyIsInNjb3BlcyI6W119.b2-ykbRMG75jBIdSbCm0EXaL8Z6SJPncJmPPFHi0chyaBdG0RxszWhjRtbgwk1wp-vsDLLsq3a3p96tSJmiJAZ8iF8UImUvcfe7ffla6WXM5u8tcnvgE3uXhxQ32ZeOa3J90X-OnwCCOyQJc6db_jWXo6uxx4faL8tiR3aiZJmYTiUgJodq5JGCvOnDIu8u1RD0AkX_Ml5-_C-hOs0fxxu1pRgPONCjRFIu7N2Cf68p5Tf_jEhxcF2Sj0p5AjkVGAK3l4by-gE8AVhgStXLXNypY77-6ZlKOkgYj5HWtsY-ycT5KYgFAvZnya4lsj3RNykAc4nH27twaOhHYSKJbBtJmCEwRBBPrgus9zU2z7Zm1hwhA0OGkcUwiMvV9s9V1l2ALsCKzuhqz7SuixD7WWlzfERBxS3eGEwx5qNxq7uLS4qM5dDNs2TZk_SSecGU3f_8zRcf8FW5lWZNrWGTOQOC_8urCMHQerLqRcdHHfnnP_mtM8-zAgtlKVj6rnD_4ojEfsSEs0p0fXt1RTKnQifOt5K84S4uS60WeNqs5hrgec4yHAllehRTSXOWB7ibbnhaO5_IYwXkyL-KrIyln75KrJE5LbeHwlv2M1V5iE_LsMzIRw9HLHCZ6KyQkG7WLW6qXrF94FZCZtRYZe8Ca8E4cP2ZVafwGl02IKjyunDw"
consulting_id = "omx8kwrgl5aep3nv"

headers = {'Accept': 'application/json', 'Authorization': 'Bearer '+str(access_token)}


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
        
    @task(10)
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