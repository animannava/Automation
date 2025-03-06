import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action= ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.CSS_SELECTOR,"a[href='#top']")).click().perform()