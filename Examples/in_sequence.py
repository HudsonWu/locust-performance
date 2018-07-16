class UserWorkflow(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        self.client.post("/login", {"username":"jack_sparrow", "password":"blackpearl"})

    @task(1)
    def user_workflow(self):
        self.load_home_page()
        self.get_list_of_posts()
        self.get_single_post(123)

    def load_home_page(self):
        self.client.get("/")

    def get_list_of_posts(self):
        self.client.get("/posts")

    def get_single_post(self, post_id):
        self.client.get("/posts/{}".format(post_id))