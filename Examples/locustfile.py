from locust import HttpLocust, TaskSet, task

class ForumPage(TaskSet):
    @task(20)
    def read_thread(self):
        pass
    
    @task(1)
    def new_thread(self):
        pass
    
    @task(5)
    def stop(self):
        self.interrupt()

class UserBehavior(TaskSet):
    def on_start(self):
        self.login()
        
    tasks = {ForumPage:10}.s
    
    @task
    class SubTaskSet(TaskSet):
        @task
        def my_task(self):
            pass    
    
    def login(self):
        self.client.post("/login",{"username":"ellen_key", "password":"education"})
        
    @task(2)
    def index(self):
        self.client.get("/")
    
    @task(1)
    def profile(self):
        self.client.get("/profile")
    
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
    