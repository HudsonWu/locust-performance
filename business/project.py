# -*- coding: utf-8 -*-

from locust import TaskSet, task

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijg1NTE4MWJhNTcwY2VkNzg2MDM3YTFkMjk3YzIwOWY4ZjQxNWRjNGVlMGM2N2M3MDJhN2U2NTA0Y2JiMDAxZDg4YzRiMGVmZGU1MzM2ZWU3In0.eyJhdWQiOiIyIiwianRpIjoiODU1MTgxYmE1NzBjZWQ3ODYwMzdhMWQyOTdjMjA5ZjhmNDE1ZGM0ZWUwYzY3YzcwMmE3ZTY1MDRjYmIwMDFkODhjNGIwZWZkZTUzMzZlZTciLCJpYXQiOjE1MzE3MTA2NTYsIm5iZiI6MTUzMTcxMDY1NiwiZXhwIjoxODQ3MDcwNjU2LCJzdWIiOiIzMSIsInNjb3BlcyI6W119.HUKpyEhcIuIwdzYqHI_fxH6M62NnMlaDnCel289YmH6NxKVjtgTOuqJnXQHG-hG3Hx61ix2vg4LbQI6VkXndvb7Rotdr04CWcPuwCGq2mkJEelCpc-X5pqRNsE7opoKk3saLdc1VK4tl33NPrVb1PdvMajMdq6rMWBOxQ07IqyEXRd9D-KKBb1NuDnHVW2YfhgnmjRkQu_ebZ8vBY-_VspePX252tqjmIJpJto2Mp2jRf_F-2lD0vt6UdFr6Lbz8-yJ9WhluocCigMa9p07XBT8Eh5u4CMrgAYe7szmnkow49r-0wduNiNxHCeMfEa5g7w7X_94e7rKjqJbjlSamxzH44jRLzC2PN59D4VfsBP9yw8ZdhMxs-DMaMh1hIjINLd7WfFE9NkNc5NWrApf3osAmVEUgRRknuq62wHyJYFtPdJMAhwxzTByHOMmTrNOWY5pDyyMvDp-Svf0BDkcZMKO9FnpU6xnkIoy0UC74b4GjgUvSgdj_CCmpNPoTYPx1yNR0Zg_ycDRt0uKlHXWyX4OWNvyeRua75ORHGyn8-j0mz2-qNxzbAnPholQx9r1vIVEVPwj7CnLTU_yRCxqvSA4K8HvFex6DyfIHA2fqw2gh6aa4ozz_NymsK38aSVN1Bdr-H3ow4kWJOTx5Nt5hCWqNWkI6Nw_3icPaXQxboqI"
headers = {'Accept': 'application/json', 'Authorization': 'Bearer '+str(access_token)}
consulting_id = "o803wk5py54mg6dl"

class MyProject(TaskSet):
       
    @task(10)
    def all_myprojects(self):
        self.client.get(name=u'参与项目-全部', url="/v1/self/project/list?limit=10&page=1&consulting_id=%s"% consulting_id,\
                        headers=headers)
    
    @task(8)
    def unstart_myprojects(self):
        self.client.get(name=u'参与项目-未启动', url="/v1/self/project/list?limit=10&page=1&status=1&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def inprogress_myprojects(self):
        self.client.get(name=u'参与项目-进行中', url="/v1/self/project/list?limit=10&page=1&status=2&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def search_myprojects(self):
        self.client.get(name=u'参与项目-搜索', url=u"/v1/self/project/list?limit=10&page=1&project_search=项目&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def role_myprojects(self):
        self.client.get(name=u'参与项目-协调人角色', url="/v1/self/project/list?limit=10&page=1&project_role=write_reporter&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(5)
    def stop(self):
        self.interrupt()
        
class AllProject(TaskSet):
       
    @task(10)
    def all_projects(self):
        self.client.get(name=u'所有项目-全部', url="/v1/manage/projects?limit=10&page=1&consulting_id=%s"% consulting_id,\
                        headers=headers)
    
    @task(8)
    def complete_projects(self):
        self.client.get(name=u'所有项目-已完成', url="/v1/manage/projects?limit=10&page=1&status=4&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def inprogress_projects(self):
        self.client.get(name=u'所有项目-进行中', url="/v1/manage/projects?limit=10&page=1&status=2&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def search_projects(self):
        self.client.get(name=u'所有项目-搜索', url=u"/v1/manage/projects?limit=10&page=1&project_search=项目&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(5)
    def stop(self):
        self.interrupt()
        

class ManageProject(TaskSet):
       
    @task(10)
    def all_manageprojects(self):
        self.client.get(name=u'管理项目-全部', url="/v1/self/manage/department/projects?limit=10&page=1&consulting_id=%s"% consulting_id,\
                        headers=headers)
    
    @task(8)
    def inprogress_manageprojects(self):
        self.client.get(name=u'管理项目-进行中', url="/v1/self/manage/department/projects?limit=10&page=1&status=2&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def review_manageprojects(self):
        self.client.get(name=u'管理项目-内审', url="/v1/self/manage/department/projects?limit=10&page=1&process=7&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(8)
    def search_manageprojects(self):
        self.client.get(name=u'管理项目-搜索', url=u"/v1/self/manage/department/projects?limit=10&page=1&project_search=项目&consulting_id=%s"% consulting_id,\
                        headers=headers)
        
    @task(5)
    def stop(self):
        self.interrupt()