from locust import TaskSet, HttpUser, task, constant


class MyTaskPages(TaskSet):
    @task
    def my_page2(self):
        res = self.client.get('/api/users?page=2')
        print('Called the api. response is:', res.status_code)

    @task
    def my_page3(self):
        res = self.client.get('/api/users?page=3')
        print('Called the api. response is:', res.status_code)


class MyTaskApi(TaskSet):

    @task
    def my_api(self):
        res = self.client.get('/api/users/2')
        print('Called the api. response is:', res.status_code)


class MyHttpUser(HttpUser):
    wait_time = constant(1)
    tasks = [MyTaskPages, MyTaskApi]

