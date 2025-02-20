from locators import Locators

# выход из аккаунта

class TestExitingAccount:
    def test_exiting_account(self, driver):
        # нажимаем кнопку Войти в аккаунт
        driver.find_element(Locators.BUTTON_LOG_IN_ACCOUNT).click()
        # нажимаем на кнопку Войти в форме Вход
        driver.find_element(Locators.BUTTON_IN_GO).click()
        # нажимаем на кнопку личный кабинет
        driver.find_element(Locators.BUTTON_PERSONAL_ACCOUNT).click()
        # нажимаем Выход в разделе изменения личных данных
        driver.find_element(Locators.BUTTON_EXIT).click()
       # проверяем, что мы в форме входа в аккаунт
        element = driver.find_element(Locators.TITTLE_ASSEMBLE_THE_BURGER)
        assert 'Вход' in element.text