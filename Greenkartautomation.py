import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)

searchtextbox=driver.find_element(By.XPATH,"//input[@type='search']")
searchtextbox.send_keys("ca")
time.sleep(2)
productslist=driver.find_elements(By.XPATH,"//div[@class='products']/div")

expectedlist=['Cauliflower - 1 Kg','Carrot - 1 Kg','Capsicum','Cashews - 1 Kg']
actuallist=[]

#print(expectedlist)

"""
for veg in productslist:
    #quantity =
    veg.find_element(By.XPATH, "//a[@class='increment']").click()
    time.sleep(1)"""

for veg in productslist:
    actuallist.append(veg.find_element(By.XPATH,"h4").text)
    veg.find_element(By.XPATH,"div/button").click()

#print(actuallist)
assert expectedlist==actuallist

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//div[@class='action-block']").click()

#To find out the total Quantity

quantity=driver.find_elements(By.XPATH,"//tr/td[3]/p")
qua=0
for q in quantity:
    qua+=int(q.text)
#print(qua)
Nofoquantity=driver.find_element(By.XPATH,"//body/div[@id='root']/div[@class='container']/div[@class='products-wrapper']/div[@class='products']/div[1]/br[4]").text
print(Nofoquantity)
#assert qua==int(Nofoquantity)


# To find out the total amount is matching with expected amount
prices=driver.find_elements(By.XPATH,"//tr/td[5]/p")
total=0
for price in prices:
    #print (int(prices[price.text]))
    total=total+int(price.text)
#print(f"Total price is: {total}")
totalprice=driver.find_element(By.XPATH,"//span[@class='totAmt']").text
assert total == int(totalprice)

#To Find out the discounted amount is matching with the expected amount

driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,"button[class='promoBtn']").click()
wait= WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

discountpercentage=driver.find_element(By.XPATH,"//span[@class='discountPerc']").text
discountamount=(total *int(discountpercentage[:-1]))/100
Finalamount=total-discountamount
discountedamount=driver.find_element(By.XPATH,"//span[@class='discountAmt']").text
assert float(Finalamount) == float(discountedamount)


driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
driver.find_element(By.XPATH,"//div/div[1]/select").send_keys("India")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//button[text()='Proceed']").click()