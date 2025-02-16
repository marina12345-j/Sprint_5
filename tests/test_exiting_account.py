from time import sleep
from selenium.webdriver.common.by import By
from confest import driver
from data import Data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait

# выход из аккаунта

class TestExitingAccount:
    def test_exiting_account(self, driver):
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        # нажимаем на кнопку выход
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button').click()

        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/h2')
        assert 'Вход' in element.text