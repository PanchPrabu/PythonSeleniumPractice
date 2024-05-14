import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value")== "option1":
        checkbox.click()
    if checkbox.get_attribute("id") == "checkBoxOption2":
        checkbox.click()
        assert checkbox.is_selected()
    #assert checkbox.is_selected()
        break

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio3":
        radiobutton.click()
        #assert radiobutton.is_selected()
        break

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

assert driver.find_element(By.XPATH,"//input[@name='enter-name']").is_displayed()
time.sleep(20)
