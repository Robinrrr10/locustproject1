from locust import HttpUser, constant, task, SequentialTaskSet
import re
import random


class EndToEnd(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.session = ""
        self.product = ""

    @task
    def web_ui(self):
        with self.client.get('', catch_response = True, name='UI') as response:
            print('web UI')
            if response.status_code == 200 and "Welcome to JPetStore 6" in response.text:
                response.success()
            else:
                response.failure('Welcome message unavailable')

    @task
    def enter_store(self):
        with self.client.get('/actions/Catalog.action', catch_response = True, name='Store') as response:
            print('Enter to store')
            if response.status_code == 200:
                products = ['Fish', 'Dogs', 'Cats', 'Reptiles', 'Birds']
                for eachProduct in products:
                    if eachProduct in response.text:
                        response.success()
                        try:
                            jsession = re.search(r"jsessionid=(.+?)\?", response.text) #this will geive the sessionid
                            self.session = jsession.group(1)  #this will give only first group
                        except:
                            self.session = ""
                    else:
                        response.failure(eachProduct + ' unavailable')
            else:
                response.failure('Status code not matchs')

    @task
    def sign_page(self):
        url = "/actions/Account.action;jsessionid="+ self.session +"?signonForm="
        with self.client.get(url, catch_response=True, name="signin_page") as response:
            print('Signin page')
            if response.status_code == 200 and "Please enter your username and password." in response:
                response.success()
            else:
                response.failure('Not in signin page')

    @task
    def signin_with_credential(self):
        data = {
            "username": "j2ee",
            "password": "j2ee",
            "signon": "Login"
        }
        with self.client.post('/actions/Account.action', data = data, catch_response = True, name = 'sign') as response:
            print('doing Login')
            if "Welcome ABC!" in response.text:
                response.success()
                try:
                    allProducts = re.findall(r"&categoryId=(.+?)\"", response.text)  #this will give all values
                    self.product = random.choice(allProducts)
                except AttributeError:
                    self.product = ""
            else:
                response.failure('Login failed')

    @task
    def product_page(self):
        url = "/actions/Catalog.action?viewCategory=&categoryId=" + self.product
        with self.client.get(url, catch_response = True, name = "Product page") as response:
            print('Product detail page')
            if self.product in response.text:
                response.success()
            else:
                response.failure('Product page unsuccessfull')

    @task
    def logoff(self):
        with self.client.get("/actions/Account.action?signoff=", catch_response=True, name='signoff') as response:
            print('Doing logoff')
            if 'Sign In' in response.text:
                response.success()
            else:
                response.failure('logoff unsuccessfull')


class PetStorPerf(HttpUser):
    host = "https://petstore.octoperf.com"
    tasks = [EndToEnd]
    wait_time = constant(1)