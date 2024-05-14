import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Click Here").click()

windowsopened = driver.window_handles

driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(windowsopened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text


