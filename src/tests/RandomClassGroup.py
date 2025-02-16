import time

from selenium import webdriver

from src.pages.AuthorizedUser import AuthorizedUser
from src.pages.Homepage import Homepage
from src.pages.LoginPage import LoginPage


def test_random_class_group():
    driver = webdriver.Chrome()
    driver.get("https://usosweb.amu.edu.pl")
    time.sleep(1)
    driver.maximize_window()

    homepage = Homepage(driver)
    login_page = LoginPage(driver)
    authorized = AuthorizedUser(driver)

    homepage.open_login_page()
    login_page.input_credentials()
    time.sleep(1)
    authorized.open_class_groups()
    time.sleep(1)
    authorized.get_random_class()

    time.sleep(5)