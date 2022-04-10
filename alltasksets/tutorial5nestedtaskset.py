from locust import TaskSet, task, constant, HttpUser

class MyTaskSet1(TaskSet):

    @task
    def first_api(self):
        res = self.client.get('/api/users/2')
        print('First api')

    @task
    class MyTaskSetNested(TaskSet):

        @task
        def second_api(self):
            res = self.client.get('/api/users?page=2')
            print('Second api')
            self.interrupt(reschedule = False)

class MyHttp(HttpUser):
    host = "https://reqres.in"
    tasks = [MyTaskSet1]
    wait_time = constant(1)
