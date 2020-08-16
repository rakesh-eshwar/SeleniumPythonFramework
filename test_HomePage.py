
"""
all the HomePage related test cases lets maintain here
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.HomePageData import HomePageData
import time
import pytest


## @pytest.mark.usefixtures(scope="class")
# class TestHomePage(BaseClass):
#
#     def test_formSubmission(self):
#
#         # sending driver object to page object class
#         home_page = HomePage(self.driver)
#         home_page.getName()
#         home_page.getEmail()
#         home_page.getPassword().send_keys("123")
#         time.sleep(1)
#         home_page.checkClick()
#         time.sleep(1)
#
#         #sel = Select(home_page.genderSelect())
#         #sel.select_by_visible_text("Female")
#         ### above drop down is re-usable, so put it in utilities
#         self.selectOptionByText(home_page.genderSelect(), "Male")
#
#         time.sleep(1)
#         home_page.submitButton().click()
#         time.sleep(1)
#
#         alert_text = home_page.successVerify().text
#         assert "Success" in alert_text


"""
re-writing the above code using DDT ( data driven testing )
-> Send multiple data inputs to the same test
"""

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        # creating log obj for logging
        log = self.getLogger()

        # sending driver object to page object class
        home_page = HomePage(self.driver)

        log.info("entering firstname and lastname/email : " +getData["firstname"] + getData["lastname"])
        home_page.getName().send_keys(getData["firstname"])
        home_page.getEmail().send_keys(getData["lastname"])
        log.info("entering password as '123' ")
        home_page.getPassword().send_keys("123")
        home_page.checkClick()
        log.info("Selecting Gender")
        self.selectOptionByText(home_page.genderSelect(), getData["gender"])
        home_page.submitButton().click()

        alert_text = home_page.successVerify().text
        assert "Success" in alert_text
        # refresh is done so that the first set of input data should be eliminated
        self.driver.refresh()

    # HomePageData.test_HomePage_data contains different sets of input data
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
