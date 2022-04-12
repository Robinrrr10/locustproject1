from locust import User, task, constant_pacing
import time


class MyUser(User):

    wait_time = constant_pacing(5)

    @task
    def my_task(self):
        time.sleep(2)
        print('My task. It will wait for 5 sec')