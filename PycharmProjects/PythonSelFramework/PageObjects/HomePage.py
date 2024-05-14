from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.XPATH,"//a[contains(@href,'shop')]")

    name =(By.CSS_SELECTOR,"input[name='name']")

    email =(By.NAME,"email")

    password = (By.ID,"exampleInputPassword1" )

    checkbox = (By.ID,"exampleCheck1")

    radiobutton = (By.CSS_SELECTOR,"#inlineRadio1")

    gender = (By.ID,"exampleFormControlSelect1")

    twowaydata =(By.XPATH,"(//input[@type='text'])[3]")

    submitform =(By.XPATH,"//input[@type='submit']")

    message = (By.CLASS_NAME,"alert-success")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def selectCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def selectRadiobutton(self):
        return self.driver.find_element(*HomePage.radiobutton)

    def genderSelection(self):
        return self.driver.find_element(*HomePage.gender)

    def dataBinding(self):
        return self.driver.find_element(*HomePage.twowaydata)

    def formSubmit(self):
        return self.driver.find_element(*HomePage.submitform)

    def getMessageText(self):
        return self.driver.find_element(*HomePage.message)


