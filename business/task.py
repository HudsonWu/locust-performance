# -*- coding: utf-8 -*-

from locust import TaskSet, task

# 测试服务器
# access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijg1NTE4MWJhNTcwY2VkNzg2MDM3YTFkMjk3YzIwOWY4ZjQxNWRjNGVlMGM2N2M3MDJhN2U2NTA0Y2JiMDAxZDg4YzRiMGVmZGU1MzM2ZWU3In0.eyJhdWQiOiIyIiwianRpIjoiODU1MTgxYmE1NzBjZWQ3ODYwMzdhMWQyOTdjMjA5ZjhmNDE1ZGM0ZWUwYzY3YzcwMmE3ZTY1MDRjYmIwMDFkODhjNGIwZWZkZTUzMzZlZTciLCJpYXQiOjE1MzE3MTA2NTYsIm5iZiI6MTUzMTcxMDY1NiwiZXhwIjoxODQ3MDcwNjU2LCJzdWIiOiIzMSIsInNjb3BlcyI6W119.HUKpyEhcIuIwdzYqHI_fxH6M62NnMlaDnCel289YmH6NxKVjtgTOuqJnXQHG-hG3Hx61ix2vg4LbQI6VkXndvb7Rotdr04CWcPuwCGq2mkJEelCpc-X5pqRNsE7opoKk3saLdc1VK4tl33NPrVb1PdvMajMdq6rMWBOxQ07IqyEXRd9D-KKBb1NuDnHVW2YfhgnmjRkQu_ebZ8vBY-_VspePX252tqjmIJpJto2Mp2jRf_F-2lD0vt6UdFr6Lbz8-yJ9WhluocCigMa9p07XBT8Eh5u4CMrgAYe7szmnkow49r-0wduNiNxHCeMfEa5g7w7X_94e7rKjqJbjlSamxzH44jRLzC2PN59D4VfsBP9yw8ZdhMxs-DMaMh1hIjINLd7WfFE9NkNc5NWrApf3osAmVEUgRRknuq62wHyJYFtPdJMAhwxzTByHOMmTrNOWY5pDyyMvDp-Svf0BDkcZMKO9FnpU6xnkIoy0UC74b4GjgUvSgdj_CCmpNPoTYPx1yNR0Zg_ycDRt0uKlHXWyX4OWNvyeRua75ORHGyn8-j0mz2-qNxzbAnPholQx9r1vIVEVPwj7CnLTU_yRCxqvSA4K8HvFex6DyfIHA2fqw2gh6aa4ozz_NymsK38aSVN1Bdr-H3ow4kWJOTx5Nt5hCWqNWkI6Nw_3icPaXQxboqI"
# consulting_id = "o803wk5py54mg6dl"

# 线上服务器
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImM4ZDk4NWUzOTEyNDkzMWI1NTBhY2I2MTE1YTZjMjQxZDlhOWM4Zjk4NDZmYjFhNjRiYWEwM2MwZjMxOGJmYTBmYzY4MjBkNzYyZWFhNjRkIn0.eyJhdWQiOiIyIiwianRpIjoiYzhkOTg1ZTM5MTI0OTMxYjU1MGFjYjYxMTVhNmMyNDFkOWE5YzhmOTg0NmZiMWE2NGJhYTAzYzBmMzE4YmZhMGZjNjgyMGQ3NjJlYWE2NGQiLCJpYXQiOjE1MzE5NjM4NjQsIm5iZiI6MTUzMTk2Mzg2NCwiZXhwIjoxODQ3MzIzODY0LCJzdWIiOiIzNyIsInNjb3BlcyI6W119.iOPJVrKoYqTs55_1rS_OAU5ZlDjoVrvzuBgtY-3QjMKmUARoUOJKuKdgnE1Cmq4gj2jlBi2cuPfStRZEMlEwM7TuCU4PXYSYD4wb5hDDFqvrdgvkc6kPA3cq5bemJKQC6CeTP3PmCQ_ILyATPZAOMsMzThAvh-FCLns5W_82hNG1bn-g410KGAbH_YgiqW6VNzNE0wom4DK7niqsiL8T31mV_-FG2P7r0-lejEXEViOWhAn1zcNmEpMFjPrijfmsfH50BA0WPXP9T3SYxEYlOnD-0zP13RIx4w4NHKOpho-w4udIFmlUBL2TR0CRhN8QeY2zmqGN8uKx7rRyDBiUV-lM3BaQK3L4LAYZQ_lkgTcXnCFlYjN5rZSVxnkUUFMyW4VHUzMVK3VEzTRuYaBQb4nbxYz7zFQPVjg1BRhAVyHmRIi4mnCwMPfiRGXOQxcTfJVZKOW4bFL68Dqp6hzmkdT-iDBzPlxIScXR1tLTUgKA8XMvNHUYZbkgO1E-XHkD2Oc35HxmTC1oP1K_FR_TsNSTy-wKiKXYJ1u5OMU6o8ZAMwnxWs-3q94TC0swh--ktW9GXr_HUIIlSTeE_tBUTkV0vcLFfwTlg789ncVbr-CuP1hTCU27sleacn8SoIx9rLqkobtodTB7Hc2EaHBRL--dRDPcHfDYUQfmbG_9iQM"
consulting_id = "omx8kwrgl5aep3nv"

headers = {'Accept': 'application/json', 'Authorization': 'Bearer '+str(access_token)}


class ReceiveTask(TaskSet):
       
    @task(10)
    def all_receivetasks(self):
        self.client.get(name=u'收到任务-全部', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&consulting_id=%s"% consulting_id)
    @task(8)
    def internal_receivetasks(self):
        self.client.get(name=u'收到任务-内审', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=internal&consulting_id=%s"% consulting_id)
    @task(8)
    def check_receivetasks(self):
        self.client.get(name=u'收到任务-内审修改', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=internal_check&consulting_id=%s"% consulting_id)
    @task(8)
    def survey_receivetasks(self):
        self.client.get(name=u'收到任务-现场勘查', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser, contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=field_survey&consulting_id=%s" \
                        % consulting_id)
    @task(8)
    def testing_receivetasks(self):
        self.client.get(name=u'收到任务-现场检测', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=field_testing&consulting_id=%s"% consulting_id)
    @task(8)
    def laboratory_receivetasks(self):
        self.client.get(name=u'收到任务-实验室', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=laboratory&consulting_id=%s"% consulting_id)    
    @task(8)
    def billing_receivetasks(self):
        self.client.get(name=u'收到任务-发票', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=billing&consulting_id=%s"% consulting_id)
    @task(8)
    def other_receivetasks(self):
        self.client.get(name=u'收到任务-其他', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=other&consulting_id=%s"% consulting_id)
        
    @task(8)
    def unstart_receivetasks(self):
        self.client.get(name=u'收到任务-未开始', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=0&consulting_id=%s"% consulting_id)
    @task(8)
    def inprogress_receivetasks(self):
        self.client.get(name=u'收到任务-进行中', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=1&consulting_id=%s"% consulting_id)
    @task(8)
    def complete_receivetasks(self):
        self.client.get(name=u'收到任务-已完成', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=2&consulting_id=%s"% consulting_id)
    @task(8)
    def close_receivetasks(self):
        self.client.get(name=u'收到任务-已关闭', headers=headers, \
                        url="/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=3&consulting_id=%s"% consulting_id)
    
    @task(8)
    def search_receivetasks(self):
        self.client.get(name=u'收到任务-搜索', headers=headers, \
                        url=u"/v1/my/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&project_name=项目&consulting_id=%s"% consulting_id,)

    @task(5)
    def stop(self):
        self.interrupt()


class SendTask(TaskSet):
       
    @task(10)
    def all_sendtasks(self):
        self.client.get(name=u'创建任务-全部', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&consulting_id=%s"% consulting_id)
    @task(8)
    def internal_sendtasks(self):
        self.client.get(name=u'创建任务-内审', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=internal&consulting_id=%s"% consulting_id)
    @task(8)
    def check_sendtasks(self):
        self.client.get(name=u'创建任务-内审修改', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=internal_check&consulting_id=%s"% consulting_id)        
    @task(8)
    def survey_sendtasks(self):
        self.client.get(name=u'创建任务-现场勘查', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=field_survey&consulting_id=%s"% consulting_id)
    @task(8)
    def testing_sendtasks(self):
        self.client.get(name=u'创建任务-现场检测', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=field_testing&consulting_id=%s"% consulting_id)
    @task(8)
    def laboratory_sendtasks(self):
        self.client.get(name=u'创建任务-实验室', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=laboratory&consulting_id=%s"% consulting_id)
    @task(8)
    def billing_sendtasks(self):
        self.client.get(name=u'创建任务-发票', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=billing&consulting_id=%s"% consulting_id)
    @task(8)
    def other_sendtasks(self):
        self.client.get(name=u'创建任务-其他', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&type=other&consulting_id=%s"% consulting_id)
    
    @task(8)
    def unstart_sendtasks(self):
        self.client.get(name=u'创建任务-未开始', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=0&consulting_id=%s"% consulting_id)
    @task(8)
    def inprogress_sendtasks(self):
        self.client.get(name=u'创建任务-进行中', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=1&consulting_id=%s"% consulting_id)
    @task(8)
    def complete_sendtasks(self):
        self.client.get(name=u'创建任务-已完成', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=2&consulting_id=%s"% consulting_id)
    @task(8)
    def close_sendtasks(self):
        self.client.get(name=u'创建任务-已关闭', headers=headers, \
                        url="/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&status=3&consulting_id=%s"% consulting_id)
    
    @task(8)
    def search_sendtasks(self):
        self.client.get(name=u'创建任务-搜索', headers=headers, \
                        url=u"/v1/my/create/tasks?include=principal,executors,project,createUser,contract,projectTechnicalInstructors,projectReportUsers&limit=10&page=1&project_name=项目&consulting_id=%s" \
                        % consulting_id)
    
    @task(5)
    def stop(self):
        self.interrupt()