import random
import time

from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory

class AuthorizedUser(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    def open_custom_schedule(self, pos=0):
        self.driver.find_element(By.NAME, "mój USOSweb").click()
        widgets = self.driver.find_element(By.CLASS_NAME, "local-home-table")
        left_div = widgets.find_elements(By.XPATH, "./div")[0]
        custom_schedules_widget = left_div.find_elements(By.XPATH, "./usos-frame")[1]
        custom_schedule = custom_schedules_widget.find_elements(By.XPATH, "./div/ul/li")[pos]
        custom_schedule.find_element(By.XPATH, "./a").click()
        self.driver.find_element(By.ID, "timebase_sem").click()

    def open_class_groups(self):
        menu_left = self.driver.find_element(By.TAG_NAME, "menu-left")
        items = menu_left.find_elements(By.XPATH, "./ul/li")
        items[2].click()

    def get_random_class(self):
        classes = self.driver.find_element(By.CLASS_NAME, "student")
        links = classes.find_elements(By.XPATH, ".//a")
        random.choice(links).click()