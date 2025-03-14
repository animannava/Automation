import time

from selenium.webdriver.common.by import By

from PageObject.Payment import Payment


class Shoppage:
    def __init__(self, driver):
        driver.implicitly_wait(5)
        self.driver = driver
        self.shop=(By.XPATH, "//ul/li[2]/a[@class='nav-link']")
        self.products=(By.XPATH, "//app-card-list[@class='row']/app-card/div/div/h4/a")
        self.checkout=(By.CSS_SELECTOR, "a[class*='btn-primary']")

    def shopping(self,product):
        self.driver.find_element(*self.shop).click()
        wantedproduct = product
        listofproducts = self.driver.find_elements(*self.products)
        for product in listofproducts:
            if product.text in wantedproduct:
                #print(product.text)
                product.find_element(By.XPATH, "//button[@class='btn btn-info']").click()

    def gocart(self):
        time.sleep(5)
        self.driver.find_element(*self.checkout).click()
        paym=Payment(self.driver)
        return paym

