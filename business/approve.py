# -*- coding: utf-8 -*-

from locust import TaskSet, task

# 测试服务器
# access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijg1NTE4MWJhNTcwY2VkNzg2MDM3YTFkMjk3YzIwOWY4ZjQxNWRjNGVlMGM2N2M3MDJhN2U2NTA0Y2JiMDAxZDg4YzRiMGVmZGU1MzM2ZWU3In0.eyJhdWQiOiIyIiwianRpIjoiODU1MTgxYmE1NzBjZWQ3ODYwMzdhMWQyOTdjMjA5ZjhmNDE1ZGM0ZWUwYzY3YzcwMmE3ZTY1MDRjYmIwMDFkODhjNGIwZWZkZTUzMzZlZTciLCJpYXQiOjE1MzE3MTA2NTYsIm5iZiI6MTUzMTcxMDY1NiwiZXhwIjoxODQ3MDcwNjU2LCJzdWIiOiIzMSIsInNjb3BlcyI6W119.HUKpyEhcIuIwdzYqHI_fxH6M62NnMlaDnCel289YmH6NxKVjtgTOuqJnXQHG-hG3Hx61ix2vg4LbQI6VkXndvb7Rotdr04CWcPuwCGq2mkJEelCpc-X5pqRNsE7opoKk3saLdc1VK4tl33NPrVb1PdvMajMdq6rMWBOxQ07IqyEXRd9D-KKBb1NuDnHVW2YfhgnmjRkQu_ebZ8vBY-_VspePX252tqjmIJpJto2Mp2jRf_F-2lD0vt6UdFr6Lbz8-yJ9WhluocCigMa9p07XBT8Eh5u4CMrgAYe7szmnkow49r-0wduNiNxHCeMfEa5g7w7X_94e7rKjqJbjlSamxzH44jRLzC2PN59D4VfsBP9yw8ZdhMxs-DMaMh1hIjINLd7WfFE9NkNc5NWrApf3osAmVEUgRRknuq62wHyJYFtPdJMAhwxzTByHOMmTrNOWY5pDyyMvDp-Svf0BDkcZMKO9FnpU6xnkIoy0UC74b4GjgUvSgdj_CCmpNPoTYPx1yNR0Zg_ycDRt0uKlHXWyX4OWNvyeRua75ORHGyn8-j0mz2-qNxzbAnPholQx9r1vIVEVPwj7CnLTU_yRCxqvSA4K8HvFex6DyfIHA2fqw2gh6aa4ozz_NymsK38aSVN1Bdr-H3ow4kWJOTx5Nt5hCWqNWkI6Nw_3icPaXQxboqI"
# consulting_id = "o803wk5py54mg6dl"

# 线上服务器
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImM1NGIwOTZiM2FiMDkyZTRmYzdjZWQ4ZWRjODY5YzY2YTdlOWQ0NTZhMTUwMDJkMjU4Mzg2OTNmYWE3ZmVjYjczMmQzMzc1OWVkMTY5ZDg1In0.eyJhdWQiOiIyIiwianRpIjoiYzU0YjA5NmIzYWIwOTJlNGZjN2NlZDhlZGM4NjljNjZhN2U5ZDQ1NmExNTAwMmQyNTgzODY5M2ZhYTdmZWNiNzMyZDMzNzU5ZWQxNjlkODUiLCJpYXQiOjE1MzE3Mzg2MDYsIm5iZiI6MTUzMTczODYwNiwiZXhwIjoxODQ3MDk4NjA2LCJzdWIiOiIzNyIsInNjb3BlcyI6W119.aa9Uc7BWCaiRoAZHEjoJM1O0mpBk9mHMu8AwVJyy4xclDuPHCbFBBw0sBISHug0rY1YqW3mN5dx6-qrBO5aZgS0nrrEX4fWCJzeXUUJ6JIzMs7Yw24Yo6ZMPhfeMDWpDKd9iO8vGqS35xeA_HHMJHUq7uuOWILShHLfwHo8nPI4gCTQdeEQlq-qvxNaJDW4oNqlOTgk93BY8agzb-1qZhVkH-HyNtTGEeRSw9MY54lHvGkH5CpOcTQcg0PLbrV7coH0y2wZVJ1hVMk_S2CLbw4twgvF7PsBxwWT3D-1P76EFDZkgRNpEGPSeh5zGMVMToMUFAIkIKuJoT0C3dgA8z9X-JN60qJGyPxAFWslkI288Uxi6CwkyEFO2T4xUSEGeTyA6i_LBYLhqR8yWz2nIByXvvW2w63E9SxOAQAA8x8_LPKIUzsR0-cHa5siGpab-WbP5E06vADg_UpS9-S2fdUu0ANgboGODn_-jtrneY_xMnLafy6r02ZKzkPG0AunBzzRC_BPsfd6qaw8dXWuhM7gyfT32xfczbhhzpUiVSErsnA8qwA--xW9UthBNj-sOTsRM9SeKVCJUWSPqa9TeEH5MsRia7EXqRHSX-MFz1i4Y-lq6gbzABIWnkDY8MA35zMzQTdoz9eJi8Blngkj76HKTT5JLz9bvg7Pyroza-DU"
consulting_id = "omx8kwrgl5aep3nv"

headers = {'Accept': 'application/json', 'Authorization': 'Bearer '+str(access_token)}


class LaunchApproval(TaskSet):
       
    @task(10)
    def launch_send(self):
        self.client.get(name=u'发起-送审', headers=headers, \
                        url="/v1/self/review/audit?limit=10&page=1&type=1&consulting_id=%s"% consulting_id)
        
    @task(10)
    def launch_report(self):
        self.client.get(name=u'发起-报批', headers=headers, \
                        url="/v1/self/review/audit?limit=10&page=1&type=2&consulting_id=%s"% consulting_id)
    
    @task(10)
    def launch_record(self):
        self.client.get(name=u'发起-备案', headers=headers, \
                        url="/v1/self/review/audit?limit=10&page=1&type=3&consulting_id=%s"% consulting_id)
        
    @task(10)
    def launch_detect(self):
        self.client.get(name=u'发起-检测', headers=headers, \
                        url="/v1/self/inspect/audit?limit=10&page=1&consulting_id=%s"% consulting_id)
    
    @task(10)
    def launch_contract(self):
        self.client.get(name=u'发起-合同评审', headers=headers, \
                        url="/v1/contract-reviews/self?limit=10&page=1&created_at_min=&created_at_max=&type=5&consulting_id=%s" \
                        % consulting_id)
        
    @task(10)
    def launch_special(self):
        self.client.get(name=u'发起-特批', headers=headers, \
                        url="/v1/projectspecialapprovals?limit=10&page=1&include=projectType,user,userDepartment,sales,documentPerson&consulting_id=%s" \
                        % consulting_id)
        
    @task(10)
    def launch_issued(self):
        self.client.get(name=u'发起-签发', headers=headers, \
                        url="/v1/documentissueds?limit=10&page=1&include=project,stages&category=0&consulting_id=%s" \
                        % consulting_id, headers=headers)
    
    @task(5)
    def stop(self):
        self.interrupt()
        

class WaitApproval(TaskSet):
       
    @task(10)
    def wait_send(self):
        self.client.get(name=u'审批-送审', headers=headers, \
                        url="/v1/review/audit?limit=10&page=1&type=1&consulting_id=%s"% consulting_id)
        
    @task(10)
    def wait_report(self):
        self.client.get(name=u'审批-报批', headers=headers, \
                        url="/v1/review/audit?limit=10&page=1&type=2&consulting_id=%s"% consulting_id)
    
    @task(10)
    def wait_record(self):
        self.client.get(name=u'审批-备案', headers=headers, \
                        url="/v1/review/audit?limit=10&page=1&type=3&consulting_id=%s"% consulting_id)
        
    @task(10)
    def wait_detect(self):
        self.client.get(name=u'审批-检测', headers=headers, \
                        url="/v1/inspect/audit?limit=10&page=1&consulting_id=%s"% consulting_id)
    
    @task(10)
    def wait_contract(self):
        self.client.get(name=u'合同评审', headers=headers, \
                        url="/v1/contract-reviews?limit=10&page=1&created_at_min=&created_at_max=&type=5&consulting_id=%s" \
                        % consulting_id)
        
    @task(10)
    def wait_special(self):
        self.client.get(name=u'审批-特批', headers=headers, \
                        url="/v1/my/specialapprovalstages?limit=10&page=1&include=projectType, user,creator,approval&consulting_id=%s" \
                        % consulting_id)
        
    @task(10)
    def wait_issued(self):
        self.client.get(name=u'审批-签发', headers=headers, \
                        url="/v1/my/documentissuedstages?limit=10&page=1&include=documentIssued,project,createUser&category=0&consulting_id=%s" \
                        % consulting_id)
    
    @task(5)
    def stop(self):
        self.interrupt()