import time

from selenium import webdriver

from src.pages.Homepage import Homepage
from src.pages.Katalog import Katalog


def test_search_katalog():
    driver = webdriver.Chrome()
    driver.get("https://usosweb.amu.edu.pl")
    time.sleep(1)
    driver.maximize_window()

    time.sleep(1)
    homepage = Homepage(driver)

    time.sleep(1)
    katalog = Katalog(driver, "DWDTLI")

    homepage.open_katalog()
    time.sleep(1)
    katalog.input_course_code()

    time.sleep(5)