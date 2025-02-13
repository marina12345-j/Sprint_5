from confest import driver
from selenium.webdriver.common.by import By

#регистрация
class TestNameLoginPassword:

    def test_name_check(self, driver):
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a/p').click()
        # driver.find_element(Locators.TEXT_NAME_INPUT).click()

        # нажимаем на кнопку зарегистрироваться
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
        #заполняем поле имя
        name_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        name_input.send_keys('Жмайлова Марина Анатольевна')
        assert  name_input is not None

    def test_mail_check(self, driver):
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '/html/body/div/div/header/nav/a').click()
        # нажимаем на кнопку зарегистрироваться
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
        # заполняем поле e-mail
        mail_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        mail_input.send_keys('jmailovamarina1825@yandex.ru')
        assert 'jmailovamarina1825@yandex.ru' in  mail_input.text

    def test_password_check(self, driver):
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '/html/body/div/div/header/nav/a').click()
        # нажимаем на кнопку зарегистрироваться
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
        # заполняем поле пароль
        password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
        password_input.send_keys('GoodLife')
        assert len(password_input.text) > 6, "Ваш пароль меньше 6 символов"















