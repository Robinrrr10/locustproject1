from locust import HttpUser, task, constant, TaskSet
import logging  #importing python inbuild logging

class MyTaskSet(TaskSet):

    @task
    def get_users(self):
        with self.client.get('/api/users?page=2', catch_response = True, name = 'page api') as response:
            logging.info('Response is: ' + response.text)  #way to create logs
            if response.elapsed.total_seconds() < 2:
                logging.debug('Response code is: ' + str(response.status_code))
                logging.debug('Response time is: ' + str(response.elapsed.total_seconds()))
                response.success()
            else:
                logging.debug('Response code is: ' + str(response.status_code))
                logging.debug('Response time is: ' + str(response.elapsed.total_seconds()))
                response.failure('Response takes more than 2 sec')


class MyHttpUsers(HttpUser):
    host = "https://reqres.in"
    tasks = [MyTaskSet]
    wait_time = constant(1)