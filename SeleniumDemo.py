from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Ani")
driver.find_element(By.NAME,"email").send_keys("ani.m@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
driver.find_element(By.XPATH,"//input[@type='date']").send_keys("04/16/1985")
driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
#driver.find_element(By.XPATH,("//input[@id='exampleFormControlSelect1'])[1]")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello")
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message
print("pass")

#driver.close()
time.sleep(30)






