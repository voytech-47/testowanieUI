import json

from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory

class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    def get_credentials(self):
        with open("..\\..\\credentials.json") as json_file:
            data = json.load(json_file)
            username = data["username"]
            password = data["password"]
            return username, password

    def input_credentials(self):
        username, password = self.get_credentials()
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.NAME, "submit").click()

