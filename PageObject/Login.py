from selenium.webdriver.common.by import By

from PageObject.Shop import Shoppage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username=(By.ID, "username")
        self.password=(By.ID, "password")
        self.submit=(By.ID, "signInBtn")

    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.submit).click()
        shopping = Shoppage(self.driver)
        return shopping