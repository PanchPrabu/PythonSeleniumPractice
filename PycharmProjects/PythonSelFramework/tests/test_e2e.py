import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass

#pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        #self.driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
        log.info("Getting all the card titles:")
        #checkoutpage = CheckOutPage(self.driver)
        products = checkoutpage.getCardTitles()
        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        print(len(products))


# THe below hidden code is previously used in our program.
# Due to changes made by Rahul in his program for Framework Explanation, i am modifying my code
       # for product in products:
       #      productName = product.find_element(By.XPATH, "div/h4/a").text
       #     if productName == "Blackberry":
       #        product.find_element(By.XPATH, "div/button").click()
        i = -1
        for product in products:
            i = i + 1
            cardText = product.text
            log.info(cardText)
           # print(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()
        checkoutpage.ShopPageCheckoutButton().click()
        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmpage = checkoutpage.FinalCheckoutButton()
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        log.info("Entering the country name as Ind")
        #confirmpage = ConfirmPage(self.driver)
        confirmpage.GetCountryValue().send_keys("Ind")
        #self.driver.find_element(By.ID, "country").send_keys("Ind")
        self.VerifyLinkPresence("India")
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        confirmpage.SelectCountryValue().click()
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmpage.SelectCheckBox().click()
        #self.driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
        confirmpage.SubmitCheckBox().click()
        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        SuccessText = confirmpage.MessageValidagtion().text
        #self.SuccessText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text received from the application is "+SuccessText)
        #print(SuccessText)

        assert "Success! Thank you!" in SuccessText



