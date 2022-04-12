from locust import User, constant, task

class MyUser(User):

    wait_time = constant(2)

    @task
    def my_task(self):
        print('My task. It will wait for 2 sec as constant is 2 sec')