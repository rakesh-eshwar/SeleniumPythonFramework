"""
Setup and TearDown :
-> Browser Invocation and browser closing is being written as part of fixture
"""

# import pytest
import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



# ============== below commented code is without POM ( Page Object Model )

# #@pytest.mark.usefixtures(scope="class")
# class TestOne(BaseClass):
#
#     def test_e2e(self):
#
#         all_products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
#
#         # here do not write all, concatenate remaining one ( //div[@class='card h-100']/div[1]/h4/a )
#         for each_product in all_products:
#             product_name = each_product.find_element_by_xpath("div[1]/h4/a").text
#             if product_name == "Blackberry":
#                 # add the item to cart  ( //div[@class='card h-100']/div[2]/button ) take only last xpath
#                 each_product.find_element_by_xpath("div[2]/button").click()
#
#
#         time.sleep(3)
#         self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
#
#         # Step : 3,4     check for blackberry ( VALIDATE )
#         time.sleep(2)
#         assert self.driver.find_element_by_link_text("Blackberry").is_displayed()
#         self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
#         time.sleep(2)
#
#         # Step 5
#         self.driver.find_element_by_id("country").send_keys("India")
#         time.sleep(8)
#         WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
#         self.driver.find_element_by_link_text("India").click()
#
#         # step 6
#         self.driver.find_element_by_xpath("//label[contains(text(),'I agree with the')]").click()
#         self.driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()
#         assert self.driver.find_element_by_xpath("//*[contains(text(),'Success!')]").is_displayed()
#
#
#         self.driver.get_screenshot_as_file("C:/Users/RakeshE-1763/PycharmProjects/SeleniumPythonPyTest/screenshot.png")



"""
re-writing the code using POM 
"""

class TestOne(BaseClass):

    def test_e2e(self):
        # creating log obj for logging
        log = self.getLogger()

        # sending driver object to page object class
        home_page = HomePage(self.driver)

        # clicks and returns the next page's object ( checkout page )
        check_out_page = home_page.shopItems()
        card_name = check_out_page.addName
        card_footer = check_out_page.addFooter

        log.info("getting all the card titles")
        cards = check_out_page.getCardTitles()

        for card in cards:
            each_card_name = card.find_element_by_xpath(card_name).text
            log.info("card name is :"+each_card_name)
            if each_card_name == "Blackberry":
                card.find_element_by_xpath(card_footer).click()

        # click checkout button after adding to cart
        check_out_page.checkoutButton().click()

        # check for blackberry ( VALIDATE ) and click checkout again
        assert self.driver.find_element_by_link_text("Blackberry").is_displayed()
        confirm_page = check_out_page.validateCheckoutButton()

        # confirm page actions
        log.info("entering country name as India")
        confirm_page.countryInput().send_keys("India")

        # wait for india to be displayed and then click india
        self.verifyLinkPresence("India")
        confirm_page.selectIndia().click()

        # select agree , click purchase button, verify string "success"
        confirm_page.selectAgree().click()
        confirm_page.purchaseButton().click()
        log.info("verifying by searching for success word")
        assert confirm_page.successPurchase().is_displayed()

        self.driver.get_screenshot_as_file("C:/Users/RakeshE-1763/PycharmProjects/SeleniumPythonPyTest/screenshot.png")

