
from locators import Locators

# переход из личного кабинета в конструктор
class TestDesignerLogo:
    # по клику Конструктор
    def test_designer(self, driver):
        # нажимаем на кнопку личный кабинет для авторизации
        driver.find_element(Locators.BUTTON_PERSONAL_ACCOUNT).click()
        # нажимаем на кнопку Войти в форме Вход
        driver.find_element(Locators.BUTTON_IN_GO).click()
        # нажимаем на кнопку Личный кабинет для входа в форму личного кабинета
        driver.find_element(Locators.BUTTON_PERSONAL_ACCOUNT).click()
        # нажимаем на кнопку Конструктор
        driver.find_element(Locators.BUTTON_REGISTER).click()
        element = driver.find_element(Locators.TITTLE_ASSEMBLE_THE_BURGER)
        assert 'Соберите бургер' in element.text

    #  по клику Логотип
    def test_logo(self, driver):
        # нажимаем на кнопку личный кабинет
        driver.find_element(Locators.BUTTON_PERSONAL_ACCOUNT).click()
        # нажимаем на кнопку Войти в форме Вход
        driver.find_element(Locators.BUTTON_IN_GO).click()
        # нажимаем на кнопку Личный кабинет для входа в форму личного кабинета
        driver.find_element(Locators.BUTTON_PERSONAL_ACCOUNT).click()
        # нажимаем на логотип
        driver.find_element(Locators.BUTTON_STELLAR_BURGERS).click()
        element = driver.find_element(Locators.TITTLE_ASSEMBLE_THE_BURGER)
        assert 'Соберите бургер' in element.text
