from locust import SequentialTaskSet, constant, task, HttpUser


class MySequentialTask(SequentialTaskSet):

    @task
    def api_one(self):
        self.client.get('/api/users?page=2')
        print('First api')

    @task
    def api_second(self):
        self.client.get('/api/users/5')
        print('Second api')


class MyHttpUser(HttpUser):
    host = "https://reqres.in"
    tasks = [MySequentialTask]
    wait_time = constant(1)