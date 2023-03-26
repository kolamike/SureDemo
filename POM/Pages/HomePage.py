from selenium.webdriver.common.by import By

from POM.Pages.BasePage import BasePage


class HomePage(BasePage):
    HEADER = (By.CSS_SELECTOR, ".AdminDashboardWrapper_CurrentRoute__EVdDW")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "account-name ")
    SETTINGS_ICON = (By.ID, "__NEXT_DATA__")
    PAYROLL = (By.CSS_SELECTOR, "button[type = 'submit']")
    TRANSACTIONS = (By.LINK_TEXT, "Transactions")
    EMPLOYEES = (By.LINK_TEXT, "Employees")
    HOME_LINK = (By.LINK_TEXT, "Home")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self,title):
        return self.get_title(title)

    def is_home_icon_exist(self):
        return self.is_visible(self.HOME_LINK)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    # def get_account_name(self):
    #     if self.is_visible(self.ACCOUNT_NAME):
    #         return self.get_element_text(self.ACCOUNT_NAME)
