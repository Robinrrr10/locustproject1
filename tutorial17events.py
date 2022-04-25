from locust import HttpUser, task, constant, SequentialTaskSet
from locust import events

import logging


@events.spawning_complete.add_listener
def spawn_users(user_count, **kwargs):
    print("Spawned users...", user_count, " users.")


@events.request_success.add_listener
def success_message(**kwargs):
    print("Test got passed successfully")

@events.request_failure.add_listener
def failure_message(**kwargs):
    print("Test got failed")

@events.quitting.add_listener
def message_after_finishing(environment, **kwargs):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test fails with fail ratio > 0.1")
        environment.process_exit_code = 1
        print(environment.process_exit_code)

    else:
        environment.process_exit_code = 0
        print(environment.process_exit_code)


class MyLoadTest(SequentialTaskSet):

    @task
    def home_page(self):
        self.client.get("/", name="TOO_Success_Request")
        self.client.get("/failed", name="TOO_Fail_Request")


class MyUser(HttpUser):
    wait_time = constant(1)
    tasks = [MyLoadTest]