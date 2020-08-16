"""
Have all the objects of CheckoutPage here
"""


from pageObjects.ConfirmPage import ConfirmPage
from selenium.webdriver.common.by import By



class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver
        self.addFooter = "div[2]/button"
        self.addName = "div[1]/h4/a"


    # creating var_obj for element property in Checkout page
    card_title = (By.XPATH, "//div[@class='card h-100']")
    checkout_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    validate_checkout_button = (By.XPATH, "//button[@class='btn btn-success']")


    # call these methods from test case to perform operation on elements in web page
    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.card_title)

    def checkoutButton(self):
        return self.driver.find_element(*CheckOutPage.checkout_button)

    def validateCheckoutButton(self):
        self.driver.find_element(*CheckOutPage.validate_checkout_button).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
