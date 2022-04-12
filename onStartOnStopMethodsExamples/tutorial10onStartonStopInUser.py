from locust import User, task, constant


class MyUser(User):
    wait_time = constant(1)

    def on_start(self):
        print('Start')

    @task
    def my_task1(self):
        print('task 1')

    @task
    def my_task2(self):
        print('task 2')

    def on_stop(self):
        print('Stop')