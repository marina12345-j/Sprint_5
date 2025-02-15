import pytest
from selenium import webdriver
from data import Data

#from data import Data

@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.STELLARBURGERS_URL)

    yield  chrome_driver

    chrome_driver.quit()