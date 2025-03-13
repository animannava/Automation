from selenium.webdriver.common.by import By


class Payment:
    def __init__(self, driver):
        self.driver = driver
        self.checkout = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def finalcheckout(self):
        self.driver.find_element(*self.checkout).click()