import json
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

Input_file_path="C:\\Automation\\RetailShopping\\Inputfile.json"
with open(Input_file_path,"r") as f:
    inputdata=json.load(f)
    inputlist=inputdata["data"]


@pytest.mark.parametrize("inputlist_item",inputlist)
def test_e2e(browserinvoking,inputlist_item):
    inputbrowser=inputlist_item["browser"]
    for browser in inputbrowser:
        driver = browserinvoking
    #driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    login=LoginPage(driver)
    shopping=login.login(inputlist_item["username"],inputlist_item["password"])
    shopping.shopping(inputlist_item["product"])
    pay=shopping.gocart()
    pay.finalcheckout()
    ship=Shipping(driver)
    ship.shiptoadd()

