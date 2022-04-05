from locust import User, task, constant


class MyUsers(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print("launch da")

    @task
    def search(self):
        print("search da")


class MyUsers2(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch2(self):
        print("launch 2 da")

    @task
    def search2(self):
        print("search 2 da")
