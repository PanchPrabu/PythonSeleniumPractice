import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name = "Prabu"
name1 = "Panch"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
Alert = driver.switch_to.alert
Message=Alert.text
print(Message)
assert name1 in Message
Alert.accept()

time.sleep(20)
