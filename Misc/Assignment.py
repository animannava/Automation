import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH,"//a[@class='blinkingText']").click()
childwindow=driver.window_handles
driver.switch_to.window(childwindow[1])
email=driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.XPATH,"//input[@id='signInBtn']").click()
wait=WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

