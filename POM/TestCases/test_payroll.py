import pytest

from POM.Configurations.Config import TestData
from POM.Pages.HomePage import HomePage
from POM.Pages.LoginPage import LoginPage
from POM.TestCases.test_base import BaseTest

class Test_Payroll(BaseTest):

    @pytest.fixture()
    def test_settings_icon(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.get_header_value()
        assert homePage.get_header_value()


    def test_payroll_link_visible(self):
        self.homepage = HomePage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        view = self.loginpage.is_payroll_link_exist()
        assert view
    #
    # def test_home_icon(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #     account_name = homePage.is_home_icon_exist()
    #     assert account_name
    #
