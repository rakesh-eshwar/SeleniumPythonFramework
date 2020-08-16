"""
Have all the objects of HomePage here
"""

from pageObjects.CheckoutPage import CheckOutPage
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    # creating var_obj for element property in Home page
    shop = (By.LINK_TEXT, "Shop")
    # fill form
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit_button = (By.XPATH, "//input[@class='btn btn-success']")
    success = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    # call these methods from test case to perform operation on elements in web page
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page

    # methods for form filling test case
    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def checkClick(self):
        return self.driver.find_element(*HomePage.check)

    def genderSelect(self):
        return self.driver.find_element(*HomePage.gender)

    def submitButton(self):
        return self.driver.find_element(*HomePage.submit_button)

    def successVerify(self):
        return self.driver.find_element(*HomePage.success)
