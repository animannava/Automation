import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "a[class='nav__button-secondary btn-secondary-emphasis btn-md']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[id='username']").send_keys("anitha.mannava@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[id='password']").send_keys("Bujji00$")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
webdrivewait = WebDriverWait(driver, 10)
webdrivewait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div/a/div[@class='display-flex mt1']")))
driver.find_element(By.XPATH,"//div/a/div[@class='display-flex mt1']").click()
time.sleep(5)