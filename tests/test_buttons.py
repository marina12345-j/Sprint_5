from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from confest import driver
from data import Data
from selenium.webdriver.common.by import By


# вход
class TestButtons:

    def test_button_go_account(self, driver):    # вход по кнопке "Войти в аккаунт"
        # нажимаем на кнопку на главной форме Войти в аккаунт
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()
        # вводим почту и пароль
        mail_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        mail_input.send_keys("jmailovamarina1825@yandex.ru")
        password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        password_input.send_keys("GoodLife")
        # нажимаем на кнопку Войти
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        driver.implicitly_wait(5)
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section/h1')
        assert 'Соберите бургер' in element.text

    def test_button_personal_account(self, driver):    # вход по кнопке "Личный кабинет"
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        # вводим почту и пароль
        mail_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        mail_input.send_keys("jmailovamarina1825@yandex.ru")
        password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        password_input.send_keys("GoodLife")
        # нажимаем на кнопку войти

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        driver.implicitly_wait(5)
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
        assert 'Соберите бургер' in element.text

    def test_button_register(self, driver):     # вход через кнопку формы регистрации
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        # нажимаем на кнопку Зарегистрироваться
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
        # вводим имя, почту и пароль
        name_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        name_input.send_keys('Жмайлова Марин Анатольев')
        mail_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        mail_input.send_keys("jmailovamar1825@yandex.ru")
        password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
        password_input.send_keys("GoodLife4")
        # нажимаем на кнопку Зарегистрироваться
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        # нажимаем кнопку в форме Войти "Войти"

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        driver.implicitly_wait(5)
        #element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section/h1')
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section/h1')
        assert 'Соберите бургер' in element.text


    def test_button_recover(self, driver):     # вход через кнопку восстановления пароля
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        # нажимаем на кнопку Восстановить пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()
        # заполняем форму e-mail
        mail_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset/div/div/input')
        mail_input.send_keys("jmailovamarina1825@yandex.ru")
        # нажимаем кнопку Восстановить
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        # в форме восстановления пароля заполняем форму пароль
        new_password = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        new_password.send_keys("GoodLife1")
        driver.implicitly_wait(5)
        # заполняем форму Введите код из письма
        new_kod = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        new_kod.send_keys(1234)

        # нажимаем кнопку Сохранить
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        # нажимаем кнопку вспомнили пароль? Войти

        driver.find_element(By.XPATH,' //*[@id="root"]/div/main/div/div/p/a').click()
        driver.implicitly_wait(5)

        # заполняем восстановленные почту и пароль
        mail_input_new = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        mail_input_new.send_keys("jmailovamarina1825@yandex.ru")

        new_password = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        new_password.send_keys("GoodLife")
        # нажимаем кнопку Войти в форме вход
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
        assert 'Соберите бургер' in element.text










