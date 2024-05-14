import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//a[@class='blinkingText']").click()
windowsopened= driver.window_handles

driver.switch_to.window(windowsopened[1])
#print(driver.find_element(By.XPATH,"//a[text()='mentor@rahulshettyacademy.com']").text)
#var = driver.find_element(By.XPATH,"//a[text()='mentor@rahulshettyacademy.com']").text
message = driver.find_element(By.CSS_SELECTOR, ".red").text
print(message)
var = message.split("at")[1].strip().split(" ")[0]
driver.close()

driver.switch_to.window(windowsopened[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(var)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys(var)
driver.find_element(By.XPATH,"//input[@id='signInBtn']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

