# -*- coding: utf-8 -*-

from locust import TaskSet, task
from common import config


#项目管理

#不同权限, 获取项目列表
class ProjectPriv(TaskSet):
    
    @task(10)
    def all_myprojects(self):
        self.client.get(name=u'参与项目-全部', headers=config.headers, \
                        url="/v1/self/project/list?limit=10&page=1&consulting_id=%s"% config.consulting_id)
    
    @task(10)
    def all_projects(self):
        self.client.get(name=u'所有项目-全部', headers=config.headers, \
                        url="/v1/manage/projects?limit=10&page=1&consulting_id=%s"% config.consulting_id)
    
    @task(10)
    def all_manageprojects(self):
        self.client.get(name=u'管理项目-全部', headers=config.headers, \
                        url="/v1/self/manage/department/projects?limit=10&page=1&consulting_id=%s"% config.consulting_id)
    
    @task
    def stop(self):
        self.interrupt()
     
    
#根据项目状态进行切换
class ProjectStatus(TaskSet):
    
    @task(8)
    def unstart_myprojects(self):
        self.client.get(name=u'参与项目-未启动', headers=config.headers, \
                        url="/v1/self/project/list?limit=10&page=1&status=1&consulting_id=%s"% config.consulting_id)
    @task(8)
    def inprogress_myprojects(self):
        self.client.get(name=u'参与项目-进行中', headers=config.headers, \
                        url="/v1/self/project/list?limit=10&page=1&status=2&consulting_id=%s"% config.consulting_id)
    @task(8)
    def stop_myprojects(self):
        self.client.get(name=u'参与项目-暂停', headers=config.headers, \
                        url="/v1/self/project/list?limit=10&page=1&status=3&consulting_id=%s"% config.consulting_id)
    @task(8)
    def complete_myprojects(self):
        self.client.get(name=u'参与项目-已完成', headers=config.headers, \
                        url="/v1/self/project/list?limit=10&page=1&status=4&consulting_id=%s"% config.consulting_id)
    @task(8)
    def break_myprojects(self):
        self.client.get(name=u'参与项目-终止', headers=config.headers, \
                        url="/v1/self/project/list?limit=10&page=1&status=5&consulting_id=%s"% config.consulting_id)
    
    @task(8)
    def unstart_projects(self):
        self.client.get(name=u'所有项目-未启动', headers=config.headers, \
                        url="/v1/manage/projects?limit=10&page=1&status=1&consulting_id=%s"% config.consulting_id)
    @task(8)
    def inprogress_projects(self):
        self.client.get(name=u'所有项目-进行中', headers=config.headers, \
                        url="/v1/manage/projects?limit=10&page=1&status=2&consulting_id=%s"% config.consulting_id)
    @task(8)
    def stop_projects(self):
        self.client.get(name=u'所有项目-暂停', headers=config.headers, \
                        url="/v1/manage/projects?limit=10&page=1&status=3&consulting_id=%s"% config.consulting_id)
    @task(8)
    def complete_projects(self):
        self.client.get(name=u'所有项目-已完成', headers=config.headers, \
                        url="/v1/manage/projects?limit=10&page=1&status=4&consulting_id=%s"% config.consulting_id)
    @task(8)
    def break_projects(self):
        self.client.get(name=u'所有项目-终止', headers=config.headers, \
                        url="/v1/manage/projects?limit=10&page=1&status=5&consulting_id=%s"% config.consulting_id)
    
    @task(8)
    def unstart_manageprojects(self):
        self.client.get(name=u'管理项目-未启动', headers=config.headers, \
                        url="/v1/self/manage/department/projects?limit=10&page=1&status=1&consulting_id=%s"% config.consulting_id)
    @task(8)
    def inprogress_manageprojects(self):
        self.client.get(name=u'管理项目-进行中', headers=config.headers, \
                        url="/v1/self/manage/department/projects?limit=10&page=1&status=2&consulting_id=%s"% config.consulting_id)
    @task(8)
    def stop_manageprojects(self):
        self.client.get(name=u'管理项目-暂停', headers=config.headers, \
                        url="/v1/self/manage/department/projects?limit=10&page=1&status=3&consulting_id=%s"% config.consulting_id)
    @task(8)
    def complete_manageprojects(self):
        self.client.get(name=u'管理项目-已完成', headers=config.headers, \
                        url="/v1/self/manage/department/projects?limit=10&page=1&status=4&consulting_id=%s"% config.consulting_id)
    
    @task
    def stop(self):
        self.interrupt()    
    

#web端项目筛选功能
class ProjectFilter(TaskSet):
    
    @task(8)
    def search_myprojects(self):
        self.client.get(name=u'参与项目-搜索', headers=config.headers, \
                        url=u"/v1/self/project/list?limit=10&page=1&project_search=项目&consulting_id=%s"% config.consulting_id)
    @task(8)
    def role_myprojects(self):
        # 筛选出角色(project_role)为协调人(write_reporter)的项目
        self.client.get(name=u'参与项目-角色', headers=config.headers, \
                        url="/v1/self/project/list?limit=10&page=1&project_role=write_reporter&consulting_id=%s"% config.consulting_id)
    @task(8)
    def process_myprojects(self):
        # 筛选出进度(process)为“现场勘查”(3)的项目
        self.client.get(name=u'参与项目-进度', headers=config.headers, \
                        url="/v1/self/project/list?limit=10&page=1&process=3&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def search_projects(self):
        self.client.get(name=u'所有项目-搜索', headers=config.headers, \
                        url=u"/v1/manage/projects?limit=10&page=1&project_search=项目&consulting_id=%s"% config.consulting_id)
    @task(8)
    def process_projects(self):
        # 筛选出进度(process)为“现场勘查”(3)的项目
        self.client.get(name=u'所有项目-进度', headers=config.headers, \
                        url="/v1/manage/projects?limit=10&page=1&process=3&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def process_manageprojects(self):
        # 筛选出进度(process)为“现场勘查”(3)的项目
        self.client.get(name=u'管理项目-进度', headers=config.headers, url="/v1/self/manage/department/projects?limit=10&page=1&process=3&consulting_id=%s"% config.consulting_id)
    @task(8)
    def search_manageprojects(self):
        self.client.get(name=u'管理项目-搜索', headers=config.headers, \
                        url=u"/v1/self/manage/department/projects?limit=10&page=1&project_search=项目&consulting_id=%s"% config.consulting_id)

    @task
    def stop(self):
        self.interrupt()


class Project(TaskSet):
    
    tasks = {ProjectPriv: 10, ProjectStatus: 10, ProjectFilter: 10}
    
    @task
    def stop(self):
        self.interrupt()