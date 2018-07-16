# -*- coding: utf-8 -*-

from locust import TaskSet, task

# 测试服务器
# access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijg1NTE4MWJhNTcwY2VkNzg2MDM3YTFkMjk3YzIwOWY4ZjQxNWRjNGVlMGM2N2M3MDJhN2U2NTA0Y2JiMDAxZDg4YzRiMGVmZGU1MzM2ZWU3In0.eyJhdWQiOiIyIiwianRpIjoiODU1MTgxYmE1NzBjZWQ3ODYwMzdhMWQyOTdjMjA5ZjhmNDE1ZGM0ZWUwYzY3YzcwMmE3ZTY1MDRjYmIwMDFkODhjNGIwZWZkZTUzMzZlZTciLCJpYXQiOjE1MzE3MTA2NTYsIm5iZiI6MTUzMTcxMDY1NiwiZXhwIjoxODQ3MDcwNjU2LCJzdWIiOiIzMSIsInNjb3BlcyI6W119.HUKpyEhcIuIwdzYqHI_fxH6M62NnMlaDnCel289YmH6NxKVjtgTOuqJnXQHG-hG3Hx61ix2vg4LbQI6VkXndvb7Rotdr04CWcPuwCGq2mkJEelCpc-X5pqRNsE7opoKk3saLdc1VK4tl33NPrVb1PdvMajMdq6rMWBOxQ07IqyEXRd9D-KKBb1NuDnHVW2YfhgnmjRkQu_ebZ8vBY-_VspePX252tqjmIJpJto2Mp2jRf_F-2lD0vt6UdFr6Lbz8-yJ9WhluocCigMa9p07XBT8Eh5u4CMrgAYe7szmnkow49r-0wduNiNxHCeMfEa5g7w7X_94e7rKjqJbjlSamxzH44jRLzC2PN59D4VfsBP9yw8ZdhMxs-DMaMh1hIjINLd7WfFE9NkNc5NWrApf3osAmVEUgRRknuq62wHyJYFtPdJMAhwxzTByHOMmTrNOWY5pDyyMvDp-Svf0BDkcZMKO9FnpU6xnkIoy0UC74b4GjgUvSgdj_CCmpNPoTYPx1yNR0Zg_ycDRt0uKlHXWyX4OWNvyeRua75ORHGyn8-j0mz2-qNxzbAnPholQx9r1vIVEVPwj7CnLTU_yRCxqvSA4K8HvFex6DyfIHA2fqw2gh6aa4ozz_NymsK38aSVN1Bdr-H3ow4kWJOTx5Nt5hCWqNWkI6Nw_3icPaXQxboqI"
# consulting_id = "o803wk5py54mg6dl"

# 线上服务器
access_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImY4ODI1YjllZDU2ZDc1NDU2Y2JhYTcyNjI3NWNlMmQzZTZhYmM5ODRhMThiOWM3NzU0OWZhOGYzYTdlOGQ5YmMyMjJkZDUxZTFkMTdmMDI2In0.eyJhdWQiOiIyIiwianRpIjoiZjg4MjViOWVkNTZkNzU0NTZjYmFhNzI2Mjc1Y2UyZDNlNmFiYzk4NGExOGI5Yzc3NTQ5ZmE4ZjNhN2U4ZDliYzIyMmRkNTFlMWQxN2YwMjYiLCJpYXQiOjE1MzE3MTEwNDUsIm5iZiI6MTUzMTcxMTA0NSwiZXhwIjoxODQ3MDcxMDQ1LCJzdWIiOiIzNyIsInNjb3BlcyI6W119.b2-ykbRMG75jBIdSbCm0EXaL8Z6SJPncJmPPFHi0chyaBdG0RxszWhjRtbgwk1wp-vsDLLsq3a3p96tSJmiJAZ8iF8UImUvcfe7ffla6WXM5u8tcnvgE3uXhxQ32ZeOa3J90X-OnwCCOyQJc6db_jWXo6uxx4faL8tiR3aiZJmYTiUgJodq5JGCvOnDIu8u1RD0AkX_Ml5-_C-hOs0fxxu1pRgPONCjRFIu7N2Cf68p5Tf_jEhxcF2Sj0p5AjkVGAK3l4by-gE8AVhgStXLXNypY77-6ZlKOkgYj5HWtsY-ycT5KYgFAvZnya4lsj3RNykAc4nH27twaOhHYSKJbBtJmCEwRBBPrgus9zU2z7Zm1hwhA0OGkcUwiMvV9s9V1l2ALsCKzuhqz7SuixD7WWlzfERBxS3eGEwx5qNxq7uLS4qM5dDNs2TZk_SSecGU3f_8zRcf8FW5lWZNrWGTOQOC_8urCMHQerLqRcdHHfnnP_mtM8-zAgtlKVj6rnD_4ojEfsSEs0p0fXt1RTKnQifOt5K84S4uS60WeNqs5hrgec4yHAllehRTSXOWB7ibbnhaO5_IYwXkyL-KrIyln75KrJE5LbeHwlv2M1V5iE_LsMzIRw9HLHCZ6KyQkG7WLW6qXrF94FZCZtRYZe8Ca8E4cP2ZVafwGl02IKjyunDw"
consulting_id = "omx8kwrgl5aep3nv"

headers = {'Accept': 'application/json', 'Authorization': 'Bearer '+str(access_token)}


class LaunchApproval(TaskSet):
       
    @task(10)
    def launch_send(self):
        self.client.get(name=u'发起-送审', url="/v1/self/review/audit?limit=10&page=1&type=1&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(10)
    def launch_report(self):
        self.client.get(name=u'发起-报批', url="/v1/self/review/audit?limit=10&page=1&type=2&consulting_id=%s"% consulting_id,\
                        headers=headers)
    
    @task(10)
    def launch_record(self):
        self.client.get(name=u'发起-备案', url="/v1/self/review/audit?limit=10&page=1&type=3&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(10)
    def launch_detect(self):
        self.client.get(name=u'发起-检测', url="/v1/self/inspect/audit?limit=10&page=1&consulting_id=%s"% consulting_id,\
                        headers=headers)
    
    @task(10)
    def launch_contract(self):
        self.client.get(name=u'发起-合同评审', url="/v1/contract-reviews/self?limit=10&page=1&created_at_min=&created_at_max=\
        &type=5&consulting_id=%s"% consulting_id, headers=headers)
        
    @task(10)
    def launch_special(self):
        self.client.get(name=u'发起-特批', url="/v1/projectspecialapprovals?limit=10&page=1&include=projectType,\
        user,userDepartment,sales,documentPerson&consulting_id=%s"% consulting_id, headers=headers)
        
    @task(10)
    def launch_issued(self):
        self.client.get(name=u'发起-签发', url="/v1/documentissued?limit=10&page=1&include=\
        project,stages&category=0&consulting_id=%s"% consulting_id, headers=headers)
    
    @task(5)
    def stop(self):
        self.interrupt()
        

class WaitApproval(TaskSet):
       
    @task(10)
    def wait_send(self):
        self.client.get(name=u'审批-送审', url="/v1/review/audit?limit=10&page=1&type=1&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(10)
    def wait_report(self):
        self.client.get(name=u'审批-报批', url="/v1/review/audit?limit=10&page=1&type=2&consulting_id=%s"% consulting_id,\
                        headers=headers)
    
    @task(10)
    def wait_record(self):
        self.client.get(name=u'审批-备案', url="/v1/review/audit?limit=10&page=1&type=3&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(10)
    def wait_detect(self):
        self.client.get(name=u'审批-检测', url="/v1/inspect/audit?limit=10&page=1&consulting_id=%s"% consulting_id,\
                        headers=headers)
    
    @task(10)
    def wait_contract(self):
        self.client.get(name=u'合同评审', url="/v1/contract-reviews?limit=10&page=1&created_at_min=&created_at_max=\
        &type=5&consulting_id=%s"% consulting_id, headers=headers)
        
    @task(10)
    def wait_special(self):
        self.client.get(name=u'审批-特批', url="/v1/my/specialapprovalstages?limit=10&page=1&include=projectType,\
        user,creator,approval&consulting_id=%s"% consulting_id, headers=headers)
        
    @task(10)
    def wait_issued(self):
        self.client.get(name=u'审批-签发', url="/v1/my/documentissuedstages?limit=10&page=1&include=\
        documentIssued,project,createUser&category=0&consulting_id=%s"% consulting_id, headers=headers)
    
    @task(5)
    def stop(self):
        self.interrupt()