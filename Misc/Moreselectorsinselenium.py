from select import select
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Register here").click()
driver.implicitly_wait(60)
driver.find_element(By.XPATH,"//input[@type='firstName']").send_keys("Some")
driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("one")
driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("someone100004@gmail.com")
driver.find_element(By.XPATH,"//input[@id='userMobile']").send_keys("1234506789")
phonenum=driver.find_element(By.XPATH,"//input[@id='userMobile']").get_attribute("value")
print(phonenum)
if phonenum.isnumeric():
    print("Phone Number is a number")
else:
    print("Phone Number is not a number")
#driver.find_element(By.CSS_SELECTOR,"//select[@class='custom-select ng-pristine ng-valid ng-touched']").send_keys("1")
driver.find_element(By.XPATH,"//input[@value='Female']").click()
driver.find_element(By.XPATH,"//input[@id='userPassword']").send_keys("Le@rningSelenium04")
driver.find_element(By.CSS_SELECTOR,"input[id='confirmPassword']").send_keys("Le@rningSelenium04")
driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
dropdown = Select(driver.find_element(By.XPATH,"//form/div[3]/div[1]/select"))
dropdown.select_by_index(1)
driver.close()
"""if driver.find_element(By.PARTIAL_LINK_TEXT,"Account") is not None:
    print("Registration successful")
else:
    print("Registration failed")"""

