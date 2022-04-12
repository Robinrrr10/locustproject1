from locust import HttpUser, task, constant

class MyHttpUsers(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)

    @task
    def get_users(self):
        self.client.get('/api/users?page=2')

    @task
    def create_user(self):
        self.client.post('/api/users', data='''{ "name": "morpheus", "job": "leader" }''')