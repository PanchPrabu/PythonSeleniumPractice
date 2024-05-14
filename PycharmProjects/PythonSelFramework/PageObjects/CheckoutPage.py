from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver =driver


    cardtitle = (By.CSS_SELECTOR,".card-title a")
    cardfooter = (By.CSS_SELECTOR,".card-footer button")
    shoppagecheckout =(By.CSS_SELECTOR,"a[class*='btn-primary']")
    finalcheckout =(By.XPATH,"//button[@class='btn btn-success']")

    #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardtitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardfooter)

    def ShopPageCheckoutButton(self):
        return self.driver.find_element(*CheckOutPage.shoppagecheckout)

    def FinalCheckoutButton(self):
        self.driver.find_element(*CheckOutPage.finalcheckout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage




