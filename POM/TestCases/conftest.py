import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from POM.Configurations.Config import TestData
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    driver_service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.get("https://salad-revamp.vercel.app/company/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

