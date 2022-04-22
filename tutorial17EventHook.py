from locust import HttpUser, task, constant
from locust.event import EventHook

send_email_message = EventHook()
send_slack_message = EventHook()

def email(a, b, request_id, message=None, **kwargs):
    print("Sending:", message, " in email for request id:", request_id)

send_email_message.add_listener(email)


def slack(a, b, request_id, message=None, **kwargs):
    print("Sending:", message, " in slack message for request id:", request_id)

send_slack_message.add_listener(slack)


class MyHttpUsers(HttpUser):
    wait_time = constant(1)

    @task
    def home_page(self):
        res = self.client.get("/", name="TOO_Homepage")
        if res.status_code == 200:
            send_email_message.fire(a=1, b=2, request_id=1, message="Success")
            send_slack_message.fire(a=1, b=2, request_id=2, message="Success")
        else:
            send_email_message.fire(a=1, b=2, request_id=1, message="Failed")
            send_slack_message.fire(a=1, b=2, request_id=2, message="Failed")

        res = self.client.get('/test', name="TOO_FailedHomepage")
        if res.status_code == 200:
            send_email_message.fire(a=1, b=2, request_id=3, message="Success")
            send_slack_message.fire(a=1, b=2, request_id=4, message="Success")
        else:
            send_email_message.fire(a=1, b=2, request_id=3, message="Failed")
            send_slack_message.fire(a=1, b=2, request_id=4, message="Failed")