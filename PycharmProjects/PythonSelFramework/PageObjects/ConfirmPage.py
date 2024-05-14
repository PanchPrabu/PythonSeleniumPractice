from selenium.webdriver.common.by import By
 

class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver


    countryvalue = (By.ID,"country")
    #self.driver.find_element(By.ID, "country").send_keys("Ind")

    selectcountry = (By.LINK_TEXT,"India")
    #self.driver.find_element(By.LINK_TEXT, "India").click()

    selectcheckbox =(By.CSS_SELECTOR,"div[class='checkbox checkbox-primary']")


    #self.driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()

    submitcheckbox =(By.XPATH,"//input[@type='submit']")

    #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    messagevalidation = (By.CLASS_NAME,"alert-success")
    #self.SuccessText = self.driver.find_element(By.CLASS_NAME, "alert-success").

    def GetCountryValue(self):
        return self.driver.find_element(*ConfirmPage.countryvalue)

    def SelectCountryValue(self):
        return self.driver.find_element(*ConfirmPage.selectcountry)

    def SelectCheckBox(self):
        return self.driver.find_element(*ConfirmPage.selectcheckbox)

    def SubmitCheckBox(self):
        return self.driver.find_element(*ConfirmPage.submitcheckbox)

    def MessageValidagtion(self):
        return self.driver.find_element(*ConfirmPage.messagevalidation)