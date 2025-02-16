from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory import PageFactory
from selenium.webdriver.common.by import By

class Katalog(PageFactory):
    _course_code = None

    def __init__(self, driver, course_code):
        self.driver = driver
        self.course_code = course_code

    def input_course_code(self):
        outer_text = self.driver.find_element(By.NAME, "_prz_kod_pattern")
        shadow_root_1 = outer_text.shadow_root
        selector = shadow_root_1.find_element(By.ID, "selector")
        shadow_root_2 = selector.shadow_root
        input_wrapper = shadow_root_2.find_element(By.ID, "input-cont")
        input_area = input_wrapper.find_element(By.TAG_NAME, "input")
        input_area.send_keys(self.course_code)
        input_area.send_keys(Keys.RETURN)

