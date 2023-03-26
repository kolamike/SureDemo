from selenium.webdriver.common.by import By
from POM.Configurations.Config import TestData
from POM.Pages.BasePage import BasePage
from POM.Pages.HomePage import HomePage


class LoginPage(BasePage):

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type = 'submit']")
    SIGNUP_LINK = (By.CSS_SELECTOR, '.MerchantLogin_createAcctLink__Ydev9')
    # SIGNIN_LINK = (By.CSS_SELECTOR, ".Signup_createAcctLink__Bi_qC")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # def sign_in(self, by_locator):
    #     self.do_click(self.SIGNIN_LINK)
    # def get_element(self, by_locator):
    #     return self.get_element(self.SIGNIN_LINK)

    def get_login_page_title(self,title):
        get_title = self.driver.title
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)





