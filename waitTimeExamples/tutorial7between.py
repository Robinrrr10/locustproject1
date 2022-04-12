from locust import task, User, between


class MyUser(User):
    wait_time = between(2, 5)

    @task
    def my_task(self):
        print('This task will randomly wait between 2 to 5 sec')