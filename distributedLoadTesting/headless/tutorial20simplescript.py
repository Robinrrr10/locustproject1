from locust import HttpUser, task, constant

class MyHttpUser(HttpUser):
   wait_time = constant(1)
   host = "https://reqres.in"

   @task
   def get_api(self):
      self.client.get("/")