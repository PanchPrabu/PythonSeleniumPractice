import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#Asssignment 2 - Here next 2 liness i am creating only expected and actual list
ExpectedList=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
ActualList=[]
######
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
assert count >0
for result in results:
    ActualList.append(result.find_element(By.XPATH,"h4").text) # Assignment 2 covered
    result.find_element(By.XPATH,"div/button").click()
print(ActualList) # Assignment 2 covered
print(ExpectedList) # Assignment 2 covered
assert ActualList == ExpectedList
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#Sum Validations
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum=0
for price in prices:
    sum=sum+int(price.text)

print(sum)
total=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == total


driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
#time.sleep(5)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

# Assignment 1
total = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
AfterDiscount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(total)
print(AfterDiscount)
#print(type(total))
#print(type(AfterDiscount))

assert AfterDiscount < total
