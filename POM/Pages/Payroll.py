import time

from selenium.webdriver.common.by import By
from POM.Pages.HomePage import HomePage

from POM.Configurations.Config import TestData
from POM.Pages.BasePage import BasePage


class Payroll(BasePage):

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type = 'submit']")
    SIGNUP_LINK = (By.CSS_SELECTOR, '.MerchantLogin_createAcctLink__Ydev9')
    HOME = (By.LINK_TEXT, "Home")
    VIEW_PAYROLL = (By.ID, "simple-tab-0")

    PAYROLL_LINK = (By.LINK_TEXT, "Payroll")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)

    def do_payroll(self):
        self.do_click(self.PAYROLL_LINK)
        return HomePage(self.driver)

    def is_home_icon_exist(self):
        return self.is_visible(self.HOME)

    def is_payroll_link_exist(self):
        return self.is_visible(self.VIEW_PAYROLL)
