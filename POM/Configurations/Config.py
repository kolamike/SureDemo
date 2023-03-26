import pytest
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        print("Launching Chrome browser.......")
    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching Firefox browser........")
    else:
        driver=webdriver.Ie
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

class TestData():
    chrome_executable_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
#
    BASE_URL = "https://salad-revamp.vercel.app/company/login"
    USER_NAME = "kolawole.shittu+20@saladafrica.com"
    PASSWORD = "Location249@"

    LOGIN_PAGE_TITLE = "Log In to Salad"

    ACCOUNT_NAME = "naveenautomationlabs"

    HOME_PAGE_TITLE = "locals"

    HOME_PAGE_HEADER = "AdminDashboardWrapper"