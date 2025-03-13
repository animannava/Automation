import pytest
from selenium import webdriver
from urllib3 import request

def pytest_addoption(parser):
    parser.addoption(
        "--browsername",
        action="store",
        default="chrome",
        help="browser to use",
    )

@pytest.fixture(scope="function")
def browserinvoking(request):
    browser= request.config.getoption("--browsername")
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.close()
