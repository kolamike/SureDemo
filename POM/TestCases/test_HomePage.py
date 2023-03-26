import pytest

from POM.Configurations.Config import TestData
from POM.Pages.LoginPage import LoginPage
from POM.TestCases.test_base import BaseTest


class Test_Home(BaseTest):
    def test_Test_Home(self,driver):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        account_name = homePage.is_home_icon_exist()
        assert homePage.is_home_icon_exist()

    # def test_title_is(title: str):
        # def _predicate(driver):
        #     return title in driver.title
        #
        # assert _predicate == TestData.HOME_PAGE_TITLE
    @pytest.fixture()
    def test_home_page_title(self):

        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE
        return homePage

    #
    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = homePage.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER
        print(header)

    # def test_home_page_account_name(self):
    #     self.loginPage = LoginPage(self.driver)
    #     homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    #     account_name = homePage.get_account_name()
    #     assert account_name == TestData.ACCOUNT_NAME



