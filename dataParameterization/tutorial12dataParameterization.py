from locust import HttpUser, constant, task, TaskSet
from testDataUtil import CsvData

class MyTaskSet(TaskSet):

    @task
    def my_api(self):
        testData = CsvData('dataParameterization\\testData.csv').read()
        print('Request: ', testData)
        data = {
            "name": testData['name'],
            "job": testData['job']
        }
        name = 'Request for ' + testData['name']
        with self.client.post('/api/users', catch_response=True, name=name, data=data) as response:
            print('Response: ', response.text)
            if response.status_code == 201 and testData['name'] in response.text:
                response.success()
            else:
                response.failure(testData['name'] + ' not available in response')


class MyHttp(HttpUser):
    host = 'https://reqres.in'
    tasks = [MyTaskSet]
    wait_time = constant(1)