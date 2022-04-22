from locust import task, HttpUser, constant


class MyUser(HttpUser):
    wait_time = constant(1)

    def __init__(self, parent):
        super().__init__(parent)
        self.hostname = self.host

    @task
    def call_api(self):
        res = self.client.get("/", name=self.hostname)
        print("345453")
        print(res.text)