import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://amazon.com")
driver.find_element(By.ID,"#nav-link-accountList-nav-line-1").click()
driver.find_element(By.XPATH,"(//a[@class='nav-a'])[1]").click()
driver.maximize_window()
#driver.find_element(By.XPATH,"(//a[@class='nav-a'])[1]").click()
time.sleep(2)
