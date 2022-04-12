from locust import TaskSet, HttpUser, task, constant


class MyTaskPages(TaskSet):

    def on_start(self):
        print('Start seq')

    @task
    def my_page2(self):
        res = self.client.get('/api/users?page=2')
        print('Called the page 2. response is:', res.status_code)

    @task
    def my_page3(self):
        res = self.client.get('/api/users?page=3')
        print('Called the page 3. response is:', res.status_code)

    def on_stop(self):
        print('Stop seq')


class MyHttpUser(HttpUser):

    host = "https://reqres.in"
    wait_time = constant(1)
    tasks = [MyTaskPages]

    def on_start(self):
        print('Start httpuser')

    def on_stop(self):
        print('Stop httpuser')

