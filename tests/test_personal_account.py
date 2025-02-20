from conftest import driver
from locators import Locators


#переход в личный кабинет
class TestPersonalAccount:

    def test_transition_personal_account(self, driver):
        # нажимаем на кнопку личный кабинет
        driver.find_element(Locators.BUTTON_PERSONAL_ACCOUNT).click()


        element = driver.find_element(Locators.HEADING_GO)
        assert 'Вход' in element.text
