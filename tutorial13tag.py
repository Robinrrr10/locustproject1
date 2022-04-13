from locust import HttpUser, constant, task, TaskSet, tag

class MyTaskSet(TaskSet):

    @task
    @tag('mytag1')
    def my_api1(self):
        self.client.get('/api/users/1')
        print('mytag1')

    @task
    @tag('mytag2')
    def my_api2(self):
        self.client.get('/api/users/2')
        print('mytag2')

    @task
    @tag('mytag1', 'mytag2')
    def my_api3(self):
        self.client.get('/api/users/3')
        print('mytag1 mytag2')

    @task
    @tag('mytag3')
    def my_api4(self):
        self.client.get('/api/users/4')
        print('mytag3')


class MyHttp(HttpUser):
    host = 'https://reqres.in'
    tasks = [MyTaskSet]
    wait_time = constant(1)