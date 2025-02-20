from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators


# вход
class TestButtons:

    def test_button_go_account(self, driver):    # вход по кнопке "Войти в аккаунт"
        # нажимаем на кнопку на главной форме "Войти в аккаунт"
        driver.find_element(Locators.BUTTON_LOG_IN_ACCOUNT).click()
        # вводим почту и пароль
        mail_input = driver.find_element(Locators.TEXT_EMAIL_INPUT)
        mail_input.send_keys(Data.AUTH_EMAIL)
        password_input = driver.find_element(Locators.TEXT_PASSWORD_INPUT)
        password_input.send_keys(Data.AUTH_PASSWORD)
        # нажимаем на кнопку Вход в форме Вход
        driver.find_element(Locators.BUTTON_IN_GO).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Data.REGISRATION_URL))

        element = driver.find_element(Locators.TITTLE_ASSEMBLE_THE_BURGER)
        assert 'Соберите бургер' in element.text

    def test_button_personal_account(self, driver):    # вход по кнопке "Личный кабинет"
        # нажимаем на кнопку личный кабинет
        driver.find_element(Locators.BUTTON_PERSONAL_ACCOUNT).click()
        # вводим почту и пароль
        mail_input = driver.find_element(Locators.TEXT_EMAIL_INPUT)
        mail_input.send_keys(Data.AUTH_EMAIL)
        password_input = driver.find_element(Locators.TEXT_PASSWORD_INPUT)
        password_input.send_keys(Data.AUTH_PASSWORD)
        # нажимаем на кнопку войти в форме Вход
        driver.find_element(Locators.BUTTON_IN_GO).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Data.REGISRATION_URL))
        element = driver.find_element(Locators.TITTLE_ASSEMBLE_THE_BURGER)
        assert 'Соберите бургер' in element.text

    def test_button_register(self, driver):     # вход через кнопку формы регистрации
        # нажимаем на кнопку личный кабинет
        driver.find_element(Locators.BUTTON_PERSONAL_ACCOUNT).click()
        # нажимаем на кнопку Зарегистрироваться (Вы-новый пользователь?)
        driver.find_element(Locators.BUTTON_REGISTER_NEW).click()
        # вводим имя, почту и пароль
        name_input = driver.find_element(Locators.TEXT_NAME_INPUT)
        name_input.send_keys(Data.AUTH_NAME)
        mail_input = driver.find_element(Locators.TEXT_EMAIL_INPUT)
        mail_input.send_keys(Data.AUTH_EMAIL)
        password_input = driver.find_element(Locators.TEXT_PASSWORD_INPUT)
        password_input.send_keys(Data.AUTH_PASSWORD)
        # нажимаем на кнопку Зарегистрироваться
        driver.find_element(Locators.BUTTON_REGISTER).click()

        # нажимаем кнопку в форме Войти "Войти"

        driver.find_element(Locators.BUTTON_IN_GO).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Data.REGISRATION_URL))

        element = driver.find_element(Locators.TITTLE_ASSEMBLE_THE_BURGER)
        assert 'Соберите бургер' in element.text


    def test_button_recover(self, driver):     # вход через кнопку восстановления пароля
        # нажимаем на кнопку личный кабинет
        driver.find_element(Locators.BUTTON_PERSONAL_ACCOUNT).click()
        # нажимаем на кнопку Восстановить пароль
        driver.find_element(Locators.BUTTON_RECOVER_PASSWORD ).click()
        # заполняем форму e-mail
        mail_input = driver.find_element(Locators.TEXT_EMAIL_INPUT)
        mail_input.send_keys(Data.AUTH_EMAIL)

        # нажимаем кнопку Восстановить
        driver.find_element(Locators.BUTTON_RECOVER).click()
        # в форме восстановления пароля заполняем форму пароль
        new_password = driver.find_element(Locators.TEXT_PASSWORD_INPUT)
        new_password.send_keys(Data.AUTH_PASSWORD)

        # заполняем форму Введите код из письма
        new_kod = driver.find_element(Locators.COD_FROM_EMAIL)
        new_kod.send_keys(1234)

        # нажимаем кнопку Сохранить
        driver.find_element(Locators.BUTTON_SAVE).click()

        # нажимаем кнопку вспомнили пароль? Войти

        driver.find_element(Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 4).until(
            expected_conditions.visibility_of_element_located(Data.REGISRATION_URL))

       # нажимаем кнопку Войти в форме вход
        driver.find_element(Locators.BUTTON_IN_GO).click()
        element = driver.find_element(Locators.TITTLE_ASSEMBLE_THE_BURGER)
        assert 'Соберите бургер' in element.text










