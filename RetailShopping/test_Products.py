import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.Login import LoginPage
from PageObject.Payment import Payment
from PageObject.Shipping import Shipping
from PageObject.Shop import Shoppage


#@pytest.mark.usefixtures("browserinvoking")
def test_e2e(browserinvoking):
    driver = browserinvoking
    #driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    login=LoginPage(driver)
    shopping=login.login(username,password)
    shopping.shopping("iphone X")
    pay=shopping.gocart()
    pay.finalcheckout()
    ship=Shipping(driver)
    ship.shiptoadd()
    #driver.close()
