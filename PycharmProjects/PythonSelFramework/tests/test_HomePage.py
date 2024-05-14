import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass




class TestHomePage(BaseClass):


    def test_formsubmission(self,getData):
        # The below 3 lines has been already defined in conftest.py file as a fixture
       # driver = webdriver.Chrome()
       # driver.get("https://rahulshettyacademy.com/angularpractice/")
       # driver.maximize_window()
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is"+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        #homepage.getName().send_keys("Prabu")
        #driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Prabu")
        log.info("Email ID value is" + getData["secondname"])
        homepage.getEmail().send_keys(getData["secondname"])
        #homepage.getEmail().send_keys("panchatcharaprabu@gmail.com")
        #driver.find_element(By.NAME, "email").send_keys("panchatcharaprabu@gmail.com")
        #homepage.getPassword().send_keys(getData[1])
        homepage.getPassword().send_keys("Test1234%")
        #driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test1234%")
        homepage.selectCheckbox().click()
        #driver.find_element(By.ID, "exampleCheck1").click()
        homepage.selectRadiobutton().click()
        #driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
        log.info("Gender is"+getData["gender"])
        self.SelectOptionByText(homepage.genderSelection(),getData["gender"])
        #self.SelectOptionByText(homepage.genderSelection(),"Female")

        #dropdown = Select(homepage.genderSelection()).select_by_visible_text("Female")

        # Static dropdowns
        #dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        #dropdown.select_by_visible_text("Female")
        # dropdown.select_by_value()
        #dropdown.select_by_index(0)
        homepage.dataBinding().send_keys("DataAgain")
        #driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Again")
        homepage.formSubmit().click()
        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
        homepage.dataBinding().clear()
        #driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
        message = homepage.getMessageText().text
        #message = driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)
        assert "success" in message
        self.driver.refresh()

        # The below method id for tuple set of data

    #@pytest.fixture(params=[("Panch","Prabu","Male"),("Meenu","Rithu","Female")])
    #def getData(self,request):
        #return request.param
    
    # The below method is for Dictionary set of data

    #@pytest.fixture(params=[{"firstname":"Panch", "secondname":"Prabu", "gender": "Male"},{"firstname": "Meenu","secondname" : "Rithu", "gender" :"Female"}])
    #def getData(self, request):
       #return request.param
    
    # Calling the data from the TestData Class file

    @pytest.fixture(params=HomePageData.getTestData("TC2"))
    def getData(self, request):
        return request.param
    
    