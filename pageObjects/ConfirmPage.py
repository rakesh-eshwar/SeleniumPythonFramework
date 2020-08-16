"""
Have all the objects of Confirm here
"""


from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver


    # creating var_obj for element property in Confirm page
    enter_country = (By.XPATH, "//input[@id='country']")
    select_india = (By.LINK_TEXT, "India")
    select_agree = (By.XPATH, "//label[contains(text(),'I agree with the')]")
    purchase_button = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    success_purchase = (By.XPATH, "//*[contains(text(),'Success!')]")


    # call these methods from test case to perform operation on elements in web page
    def countryInput(self):
        return self.driver.find_element(*ConfirmPage.enter_country)

    def selectIndia(self):
        return self.driver.find_element(*ConfirmPage.select_india)

    def selectAgree(self):
        return self.driver.find_element(*ConfirmPage.select_agree)

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def successPurchase(self):
        return self.driver.find_element(*ConfirmPage.success_purchase)
