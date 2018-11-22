from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    
    @task
    def login(self):
        with self.client.post("/v1/client/login",\
                                    {"username":"test029@zwehs.com", "password":"123456"}) as response:
            print(response.content)
            
        
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000


class others():
    '''
    def get_token(self):
        post_data = dict(username='test029@zwehs.com', password='123456')
        with self.client.post(name='login', url="/v1/client/login",\
                                    data=post_data) as response:
            data = response.json()
            access_token = data['access_token']
            headers = {'Accept':'application/json',\
                   'Authorization':'Bearer '+str(access_token)}
            print("status_code: %s\naccess_token: %s"% (response.status_code, access_token))
    
    def get_console(self):
        
        #获取我的控制台
        #返回当前账户的角色信息
        
        print(headers)
        with self.client.get(name='console', url="/v1/web/my/console",\
                             headers=headers) as response:
            print("status_code: %s"% response.status_code)
            data = response.json()
            roles = data['data']
            for role in roles:
                if role['identity'] == "consulting":
                    consulting_id = role['identity_id']
                    consulting_name = role['name']
                    print("consulting_name: %s"% consulting_name)
                    break
            if consulting_id == "":
                print(u'当前账户不存在咨询机构角色!!!')
                exit(0)
    '''    