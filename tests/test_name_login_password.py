from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Data
from locators import Locators


#регистрация
class TestNameLoginPassword:
    def test_success_login(self, driver):
        driver.find_element(Locators.BUTTON_PERSONAL_ACCOUNT).click() # нажимаем на кнопку ЛИЧНЫЙ КАБИНЕТ
        driver.find_element(Locators.BUTTON_REGISTER_NEW).click()   # нажимаем на кнопку зарегистрироваться при авторизации (вы новый пользователь)
# Водим данные имени, email и пароля
        name_input = driver.find_element(Locators.TEXT_NAME_INPUT)
        name_input.send_keys(Data.AUTH_NAME)

        mail_input = driver.find_element(Locators.TEXT_EMAIL_INPUT)
        mail_input.send_keys(Data.AUTH_EMAIL)

        password_input = driver.find_element(Locators.TEXT_PASSWORD_INPUT)
        password_input.send_keys(Data.AUTH_PASSWORD)
        # кнопка зарегистрироваться все данные в форме уже введены
        driver.find_element(Locators.BUTTON_REGISTER).click()
        # Нажимаем на кнопку Войти в форме Вход
        driver.find_element(Locators.BUTTON_IN_GO).click()


        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.BUTTON_PLACE_ON_ORDER)) #By.XPATH, '//*[@id="root"]/div/main/div/form/button'

        ##assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        assert driver.current_url == driver.current_url.get(Data.REGISRATION_URL)




