import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(3)
elementslist=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
for a in elementslist:
    if a.text == "India":
        a.click()
        break
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"
    ##time.sleep(20)

