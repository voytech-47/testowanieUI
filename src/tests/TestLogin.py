import time

from selenium import webdriver

from src.pages.Homepage import Homepage
from src.pages.LoginPage import LoginPage


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://usosweb.amu.edu.pl")
    time.sleep(1)
    driver.maximize_window()

    homepage = Homepage(driver)
    login_page = LoginPage(driver)

    homepage.open_login_page()
    time.sleep(1)
    login_page.input_credentials()

    time.sleep(3)