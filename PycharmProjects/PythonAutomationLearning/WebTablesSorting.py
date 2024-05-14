import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browserInfoList=[]

#/Click on the header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

# collect the veggies name in the list

browserInfoList = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in browserInfoList:
    browserInfoList.append(ele.text)
print(browserInfoList)

OriginalbrowserInfoList=browserInfoList.copy()

# Sorting the veggie names collected from the browser
browserInfoList.sort()

assert browserInfoList == OriginalbrowserInfoList
