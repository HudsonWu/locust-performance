# -*- coding: utf-8 -*-

from locust import TaskSet, task, seq_task
from common import config


#审批管理

#发起的审批
class LaunchApproval(TaskSet):
    
    @task(10)
    def launch_statistics(self):
        self.client.get(name=u'发起-统计', headers=config.headers, \
                        url="/v1/self/review/count?consulting_id=%s"% config.consulting_id)
       
    @task(10)
    def launch_send(self):
        self.client.get(name=u'发起-送审', headers=config.headers, \
                        url="/v1/self/review/audit?limit=10&page=1&type=1&consulting_id=%s"% config.consulting_id)
        
    @task(10)
    def launch_report(self):
        self.client.get(name=u'发起-报批', headers=config.headers, \
                        url="/v1/self/review/audit?limit=10&page=1&type=2&consulting_id=%s"% config.consulting_id)
    
    @task(10)
    def launch_record(self):
        self.client.get(name=u'发起-备案', headers=config.headers, \
                        url="/v1/self/review/audit?limit=10&page=1&type=3&consulting_id=%s"% config.consulting_id)
        
    @task(10)
    def launch_detect(self):
        self.client.get(name=u'发起-检测', headers=config.headers, \
                        url="/v1/self/inspect/audit?limit=10&page=1&consulting_id=%s"% config.consulting_id)
    
    @task(10)
    def launch_contract(self):
        self.client.get(name=u'发起-合同评审', headers=config.headers, \
                        url="/v1/contract-reviews/self?limit=10&page=1&created_at_min=&created_at_max=&type=5&consulting_id=%s" \
                        % config.consulting_id)
        
    @task(10)
    def launch_special(self):
        self.client.get(name=u'发起-特批', headers=config.headers, \
                        url="/v1/projectspecialapprovals?limit=10&page=1&include=projectType,user,userDepartment,sales,documentPerson&consulting_id=%s" \
                        % config.consulting_id)
        
    @task(10)
    def launch_issued(self):
        self.client.get(name=u'发起-签发', headers=config.headers, \
                        url="/v1/documentissueds?limit=10&page=1&include=project,stages&category=0&consulting_id=%s" \
                        % config.consulting_id)
    
    @task(10)
    def launch_offlineReview(self):
        self.client.get(name=u'发起-线下评审', headers=config.headers, \
                        url='/v1/my/created/mettings?limit=10&page=1&type=1&consulting_id=%s'% config.consulting_id)
    
    @task(10)
    def launch_obsoleteBill(self):
        self.client.get(name=u'发起-发票作废', headers=config.headers, \
                        url='/v1/myobsoletebill?limit=10&page=1&consulting_id=%s'% config.consulting_id)
    
    @task(10)
    def launch_tender(self):
        self.client.get(name=u'发起-标书', headers=config.headers, \
                        url='/v1/my/create/tenders?limit=10&page=1&consulting_id=%s'% config.consulting_id)
    
    @task(5)
    def stop(self):
        self.interrupt()
        

#待我审批
class WaitApproval(TaskSet):
    
    @task(10)
    def wait_statistics(self):
        self.client.get(name=u'审批-统计', headers=config.headers, \
                        url="/v1/review/count?consulting_id=%s"% config.consulting_id)
        
    @task(10)
    def wait_send(self):
        self.client.get(name=u'审批-送审', headers=config.headers, \
                        url="/v1/review/audit?limit=10&page=1&type=1&consulting_id=%s"% config.consulting_id)
        
    @task(10)
    def wait_report(self):
        self.client.get(name=u'审批-报批', headers=config.headers, \
                        url="/v1/review/audit?limit=10&page=1&type=2&consulting_id=%s"% config.consulting_id)
    
    @task(10)
    def wait_record(self):
        self.client.get(name=u'审批-备案', headers=config.headers, \
                        url="/v1/review/audit?limit=10&page=1&type=3&consulting_id=%s"% config.consulting_id)
        
    @task(10)
    def wait_detect(self):
        self.client.get(name=u'审批-检测', headers=config.headers, \
                        url="/v1/inspect/audit?limit=10&page=1&consulting_id=%s"% config.consulting_id)
    
    @task(10)
    def wait_contract(self):
        self.client.get(name=u'审批-合同评审', headers=config.headers, \
                        url="/v1/contract-reviews?limit=10&page=1&created_at_min=&created_at_max=&type=5&consulting_id=%s" \
                        % config.consulting_id)
        
    @task(10)
    def wait_special(self):
        self.client.get(name=u'审批-特批', headers=config.headers, \
                        url="/v1/my/specialapprovalstages?limit=10&page=1&include=projectType, user,creator,approval&consulting_id=%s" \
                        % config.consulting_id)
        
    @task(10)
    def wait_issued(self):
        self.client.get(name=u'审批-签发', headers=config.headers, \
                        url="/v1/my/documentissuedstages?limit=10&page=1&include=documentIssued,project,createUser&category=0&consulting_id=%s" \
                        % config.consulting_id)
    
    @task(10)
    def wait_offlineReview(self):
        self.client.get(name=u'审批-线下评审', headers=config.headers, \
                        url="/v1/my/mettings?limit=10&page=1&type=1&consulting_id=%s"% config.consulting_id)
    
    @task(10)
    def wait_obsoleteBill(self):
        self.client.get(name=u'审批-发票作废', headers=config.headers, \
                        url='/v1/obsoletebill?limit=10&page=1&consulting_id=%s'% config.consulting_id)
    
    @task(10)
    def wait_tender(self):
        self.client.get(name=u'审批-标书', headers=config.headers, \
                        url='/v1/my/tender_stages?limit=10&page=1&include=tender,createUser&consulting_id=%s'% config.consulting_id)
    
    @task(5)
    def stop(self):
        self.interrupt()


class Approval(TaskSet):
    
    tasks = {LaunchApproval: 10, WaitApproval: 10}
    
    @task
    def stop(self):
        self.interrupt()    