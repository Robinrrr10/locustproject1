from locust import TaskSet, constant, task, HttpUser
import random

class MyApisTask(TaskSet):

    @task
    def get_page_api(self):
        self.client.get('/api/users?page=2')
        print('Get api page 2')

    @task
    def get_differnt_id_api(self):
        ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        random_endpoint = "/api/users/" + str(random.choice(ids))
        self.client.get(random_endpoint)
        print('Each api with id')

class MyUser(HttpUser):
    host = "https://reqres.in"
    tasks = [MyApisTask]
    wait_time = constant(1)