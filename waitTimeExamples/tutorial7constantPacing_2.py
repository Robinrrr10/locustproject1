from locust import User, task, constant_pacing
import time


class MyUser(User):

    wait_time = constant_pacing(5)

    @task
    def my_task(self):
        time.sleep(10)
        print('It will wait for 10 sec')