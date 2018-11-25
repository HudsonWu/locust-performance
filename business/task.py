# -*- coding: utf-8 -*-

from locust import TaskSet, task, seq_task
from common import config

#任务管理
class ReceiveTask(TaskSet):
    
    @task(10)
    def receive_statistics(self):
        self.client.get(name=u'收到任务-统计', headers=config.headers, \
                        url='/v1/task/join/count?type[]=all&type[]=internal&type[]=internal_check&type[]=field_survey& \
                        type[]=field_testing&type[]=laboratory&type[]=billing&type[]=other&type_array=1&consulting_id=%s"% config.consulting_id)')
       
    @task(10)
    def all_receivetasks(self):
        self.client.get(name=u'收到任务-全部', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&consulting_id=%s"% config.consulting_id)
    @task(8)
    def internal_receivetasks(self):
        self.client.get(name=u'收到任务-内审', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=internal&consulting_id=%s"% config.consulting_id)
    @task(8)
    def check_receivetasks(self):
        self.client.get(name=u'收到任务-内审修改', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=internal_check&consulting_id=%s"% config.consulting_id)
    @task(8)
    def survey_receivetasks(self):
        self.client.get(name=u'收到任务-现场勘查', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser, contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=field_survey&consulting_id=%s" \
                        % config.consulting_id)
    @task(8)
    def testing_receivetasks(self):
        self.client.get(name=u'收到任务-现场检测', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=field_testing&consulting_id=%s"% config.consulting_id)
    @task(8)
    def laboratory_receivetasks(self):
        self.client.get(name=u'收到任务-实验室', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=laboratory&consulting_id=%s"% config.consulting_id)    
    @task(8)
    def billing_receivetasks(self):
        self.client.get(name=u'收到任务-发票', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=billing&consulting_id=%s"% config.consulting_id)
    @task(8)
    def other_receivetasks(self):
        self.client.get(name=u'收到任务-其他', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=other&consulting_id=%s"% config.consulting_id)
        
    @task(8)
    def unstart_receivetasks(self):
        self.client.get(name=u'收到任务-未开始', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=0&consulting_id=%s"% config.consulting_id)
    @task(8)
    def inprogress_receivetasks(self):
        self.client.get(name=u'收到任务-进行中', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=1&consulting_id=%s"% config.consulting_id)
    @task(8)
    def complete_receivetasks(self):
        self.client.get(name=u'收到任务-已完成', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=2&consulting_id=%s"% config.consulting_id)
    @task(8)
    def close_receivetasks(self):
        self.client.get(name=u'收到任务-已关闭', headers=config.headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=3&consulting_id=%s"% config.consulting_id)
    
    @task(8)
    def search_receivetasks(self):
        self.client.get(name=u'收到任务-搜索', headers=config.headers, \
                        url=u"/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&project_name=项目&consulting_id=%s"% consulting_id,)

    @task(5)
    def stop(self):
        self.interrupt()


class SendTask(TaskSet):
    
    @task(10)
    def send_statistics(self):
        self.client.get(name=u'创建任务-统计', headers=config.headers, \
                        url="/v1/task/create/count?type[]=all&type[]=internal&type[]=internal_check&type[]=field_survey& \
                        type[]=field_testing&type[]=laboratory&type[]=billing&type[]=other&type_array=1&consulting_id=%s"% config.consulting_id)
        
    @task(10)
    def all_sendtasks(self):
        self.client.get(name=u'创建任务-全部', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&consulting_id=%s"% config.consulting_id)
    @task(8)
    def internal_sendtasks(self):
        self.client.get(name=u'创建任务-内审', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=internal&consulting_id=%s"% config.consulting_id)
    @task(8)
    def check_sendtasks(self):
        self.client.get(name=u'创建任务-内审修改', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=internal_check&consulting_id=%s"% config.consulting_id)        
    @task(8)
    def survey_sendtasks(self):
        self.client.get(name=u'创建任务-现场勘查', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=field_survey&consulting_id=%s"% config.consulting_id)
    @task(8)
    def testing_sendtasks(self):
        self.client.get(name=u'创建任务-现场检测', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=field_testing&consulting_id=%s"% config.consulting_id)
    @task(8)
    def laboratory_sendtasks(self):
        self.client.get(name=u'创建任务-实验室', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=laboratory&consulting_id=%s"% config.consulting_id)
    @task(8)
    def billing_sendtasks(self):
        self.client.get(name=u'创建任务-发票', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=billing&consulting_id=%s"% config.consulting_id)
    @task(8)
    def other_sendtasks(self):
        self.client.get(name=u'创建任务-其他', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=other&consulting_id=%s"% config.consulting_id)
    
    @task(8)
    def unstart_sendtasks(self):
        self.client.get(name=u'创建任务-未开始', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=0&consulting_id=%s"% config.consulting_id)
    @task(8)
    def inprogress_sendtasks(self):
        self.client.get(name=u'创建任务-进行中', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=1&consulting_id=%s"% config.consulting_id)
    @task(8)
    def complete_sendtasks(self):
        self.client.get(name=u'创建任务-已完成', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=2&consulting_id=%s"% config.consulting_id)
    @task(8)
    def close_sendtasks(self):
        self.client.get(name=u'创建任务-已关闭', headers=config.headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=3&consulting_id=%s"% config.consulting_id)
    
    @task(8)
    def search_sendtasks(self):
        self.client.get(name=u'创建任务-搜索', headers=config.headers, \
                        url=u"/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&project_name=项目&consulting_id=%s" \
                        % config.consulting_id)
    
    @task(5)
    def stop(self):
        self.interrupt()


class Taskb(TaskSet):
    
    tasks = {ReceiveTask: 10, SendTask: 10}
    
    @task
    def stop(self):
        self.interrupt()    
    