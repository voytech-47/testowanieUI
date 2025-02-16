import time

from selenium import webdriver

from src.pages.Homepage import Homepage


def test_katalog():
    driver = webdriver.Chrome()
    driver.get("https://usosweb.amu.edu.pl")
    time.sleep(1)
    driver.maximize_window()

    homepage = Homepage(driver)

    time.sleep(1)
    homepage.open_katalog()

    time.sleep(5)