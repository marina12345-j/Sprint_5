from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from confest import driver
from selenium.webdriver.common.by import By

#регистрация
class TestNameLoginPassword:
    def test_success_login(self, driver):
        driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a/p').click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

        name_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        name_input.send_keys('Жмайлова Марина Анатольевна')

        mail_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        mail_input.send_keys("jmailovamarina1825@yandex.ru")

        password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
        password_input.send_keys("GoodLife")

        driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/button').click()


        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/form/button')))

        ##assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

        # driver.quit()
