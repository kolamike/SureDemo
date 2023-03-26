import pytest

from POM.Configurations.Config import TestData
from POM.Pages.LoginPage import LoginPage
from POM.TestCases.test_base import BaseTest

class Test_Login(BaseTest):
    def test_signup_link_visible(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_signup_link_exist()
        assert flag

    # def test_title_is(title: str):
    #     def _predicate(driver):
    #         return title in driver.title
    #     assert _predicate

    def test_login_page_title(self):
        self.Loginpage = LoginPage(self.driver)
        title = self.Loginpage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)



