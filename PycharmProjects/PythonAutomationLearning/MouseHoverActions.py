import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.implicitly_wait(5)
driver.maximize_window()
Action = ActionChains(driver)
# Scenaior 1
Action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#Action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
# Scenario 2
Action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
Action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

time.sleep(5)
