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