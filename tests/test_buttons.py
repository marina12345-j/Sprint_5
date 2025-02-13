from confest import driver
from data import Data
from selenium.webdriver.common.by import By


# вход
class TestButtons:

    def test_button_go_account(self, driver):    # вход по кнопке "Войти в аккаунт"
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        # нажимаем на кнопку Войти
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
        assert 'Соберите бургер' in element.text

    def test_button_personal_account(self, driver):    # вход по кнопке "Личный кабинет"
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        # нажимаем на кнопку войти
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        #WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.BUTTON_PERSONAL_ACCOUNT))
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
        assert 'Соберите бургер' in element.text

    def test_button_register(self, driver):     # вход через кнопку формы регистрации
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        # нажимаем на кнопку Зарегистрироваться
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()
        # нажимаем на кнопку Уже зарегистрированы? Войти
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
        # нажимаем кнопку в форме Войти "Войти"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
        assert 'Соберите бургер' in element.text


    def test_button_recover(self, driver):     # вход через кнопку восстановления пароля
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        # нажимаем на кнопку Восстановить пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()
        # заполняем форму e-mail
        mail_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset/div/div/input')
        mail_input.send_keys(Data.AUTH_EMAIL)
        # нажимаем кнопку Восстановить
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        # в форме восстановления пароля заполняем форму пароль
        new_password = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').click()
        new_password.send_keys(Data.AUTH_PASSWORD)

        # заполняем форму Введите код из письма
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').click()
        new_password.send_keys(1234)

        # нажимаем кнопку Сохранить
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        # нажимаем кнопку войти
        driver.find_element(By.XPATH,' //*[@id="root"]/div/main/div/div/p/a').click()

        # нажимаем кнопку Войти в форме вход
        driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/button').click()
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
        assert 'Соберите бургер' in element.text










