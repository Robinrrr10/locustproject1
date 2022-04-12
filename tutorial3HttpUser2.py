from locust import HttpUser, task, constant

class MyHttpUsers(HttpUser):
    wait_time = constant(1)

    @task
    def get_users(self):
        res = self.client.get('/api/users?page=2')
        print(res.status_code)
        print(res.headers)
        print(res.text)

    @task
    def create_user(self):
        res = self.client.post('/api/users', data='''{ "name": "morpheus", "job": "leader" }''')
        print(res.status_code)
        print(res.headers)
        print(res.text)