from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory

class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    def open_katalog(self):
        self.driver.find_element(By.NAME, "katalog").click()

    def open_login_page(self):
        top_bar = self.driver.find_element(By.ID, "layout-cas-bar")
        shadow_root = top_bar.shadow_root
        shadow_root.find_element(By.ID, "actions").find_element(By.TAG_NAME, "a").click()

