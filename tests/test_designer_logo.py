#from time import sleep
#from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from confest import driver
#from data import Data
#rom locators import Locators
#from selenium.webdriver.support.wait import WebDriverWait
# переход из личного кабинета в конструктор
class TestDesignerLogo:
    def test_designer(self, driver):
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        # нажимаем на кнопку Конструктор
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p').click()
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
        assert 'Соберите бургер' in element.text


    def test_logo(self, driver):
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        # нажимаем на логотип
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/div/a/svg/g[1]').click()
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
        assert 'Соберите бургер' in element.text
