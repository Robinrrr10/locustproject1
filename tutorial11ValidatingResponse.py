from locust import HttpUser, constant, task, TaskSet


class MyTasks(TaskSet):

    @task
    def first_api(self):
        response = self.client.get('/api/users/3', name='API 1')
        print(response)  #this will just pring the status code with objectname as response

    @task
    def second_api(self):
        with self.client.get('/api/users/2', catch_response=True,name='API 2') as response:  #This will store response in a object/file name response
            result = True if 'Weaver' in response.text else False              #validating
            print(self.second_api.__name__, result)
            if result == True:
                response.success()                                     #making the test success
            else:
                response.failure('Weaver not available in response')        #this is to fail the test

    @task
    def third_api(self):
        with self.client.get('/api/users/3', catch_response=True, name='API 3') as response:
            result = True if 'raman' in response.text else False
            print(self.third_api.__name__, result)
            if result == True:
                response.success()
            else:
                response.failure('raman not available in response')


class MyHttp(HttpUser):
    host = "https://reqres.in"
    tasks = [MyTasks]
    wait_time = constant(1)