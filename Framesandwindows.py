import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR,"a[href='/frames']").click()
driver.find_element(By.CSS_SELECTOR,"a[href='/nested_frames']").click()
driver.switch_to.frame("frame-top")
frames=driver.find_element(By.XPATH,"//frameset[@name='frameset-middle']")
frameslist=frames.find_elements(By.XPATH,"//frameset/frame")

for frame in frameslist:
    print(frame.get_attribute("name"))

driver.switch_to.window(driver.current_window_handle)
print(driver.find_element(By.XPATH,"//frameset/frame[@name='frame-bottom']").get_attribute("name"))

driver.back()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"a[href='/iframe']").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").send_keys("Frame Automation")
time.sleep(5)
driver.back()
driver.back()
#driver.close()
driver.find_element(By.CSS_SELECTOR,"a[href='/windows']").click()
#driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//div/div[1]/a").click()
windowlist= driver.window_handles

a=0
for i in windowlist:
    driver.switch_to.window(windowlist[a])
    if driver.title=="New Window":
        print("We are in first child window")
    a=a+1
childwindowtext= driver.find_element(By.TAG_NAME,"h3").text
print(childwindowtext)
driver.close()
time.sleep(2)

driver.switch_to.window(windowlist[0])
parentwindowtext= driver.find_element(By.TAG_NAME,"h3").text
print(parentwindowtext)
