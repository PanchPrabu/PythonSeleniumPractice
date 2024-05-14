import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj=Service("C:/Users/USER/Desktop/Python Automaion Material/Udemy Course Materials/chromedriver-win64/chromedriver.exe")
#driver=webdriver.Chrome(service=service_obj)
driver = webdriver.Edge()

driver.get("https://icicibank.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)