from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Shipping:
    def __init__(self, driver):
        self.driver = driver
        self.country=(By.ID, "country")
        self.counlink =(By.LINK_TEXT, "India")
        self.checkbox=(By.XPATH, "//label[@for='checkbox2']")
        self.submit=(By.XPATH, "//input[@type='submit']")
        self.alert=(By.CLASS_NAME, "alert-success")


    def shiptoadd(self):
        self.driver.find_element(*self.country).send_keys("ind")
        self.driver.save_screenshot("screenshot.png")
        webdriverwait = WebDriverWait(self.driver, 10)
        webdriverwait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "India"))).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit).click()
        textmessage = self.driver.find_element(*self.alert).text
        assert 'Success' in textmessage