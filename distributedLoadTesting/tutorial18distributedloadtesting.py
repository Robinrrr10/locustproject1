from locust import HttpUser, TaskSet, task, constant


class MyTask(TaskSet):

    @task
    def call_get(self):
        self.client.get("/api/users?page=2", name="GET users Page")

    @task
    def call_get(self):
        self.client.get("/api/users/3", name="GET user 3")


class MyHttpUser(HttpUser):
    host = "https://reqres.in"
    tasks = [MyTask]
    wait_time = constant(1)