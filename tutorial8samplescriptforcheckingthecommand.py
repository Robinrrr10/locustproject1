from locust import HttpUser, task, constant


class MyHttpUser(HttpUser):
    wait_time = constant(1)

    @task
    def my_api(self):
        res = self.client.get('/api/users?page=2')
        print('Called the api. response is:', res.status_code)