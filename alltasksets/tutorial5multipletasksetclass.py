from locust import TaskSet, task, constant, HttpUser


class MyTaskSet1(TaskSet):
    @task
    def first_api(self):
        self.client.get('/api/users/2')
        print('First api')
        self.interrupt(reschedule=False)


class MyTaskSet2(TaskSet):
    @task
    def second_api(self):
        self.client.get('/api/users?page=2')
        print('Second api')
        self.interrupt(reschedule=False)


class MyHttpUser(HttpUser):
    host = "https://reqres.in"
    tasks = [MyTaskSet1, MyTaskSet2]
    wait_time = constant(1)