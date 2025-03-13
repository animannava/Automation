import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)
checkboxes=driver.find_elements(By.XPATH,"//div/div[4]/fieldset/label/input")
#print (len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        break
assert checkbox.is_selected()
#time.sleep(5)
radiobuttons=driver.find_elements(By.XPATH,"//div/div[1]/fieldset/label/input")
#print(len(radiobuttons))
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio3":
        radiobutton.click()
        break
assert radiobutton.is_selected()

#time.sleep(5)

hidetextbox=driver.find_element(By.XPATH,"//input[@id='displayed-text']")
assert hidetextbox.is_displayed()
hidebutton =driver.find_element(By.XPATH,"//input[@id='hide-textbox']")
hidebutton.click()
#time.sleep(5)
assert not hidetextbox.is_displayed()

#time.sleep(5)

displayfunction=driver.find_element(By.CSS_SELECTOR,"#name")
if displayfunction.is_displayed() == True:
    displayfunction.send_keys("Anitha")
    driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
    time.sleep(5)
    alert=driver.switch_to.alert
    alerttext=alert.text
    print(alerttext)
    assert "Anitha" in alerttext
    alert.dismiss()
    #alert.accept()

    #time.sleep(10)




