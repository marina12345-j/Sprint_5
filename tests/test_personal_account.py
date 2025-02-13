from selenium.webdriver.common.by import By
from confest import driver

#переход в личный кабинет
class TestPersonalAccount:

    def test_transition_personal_account(self, driver):
        # нажимаем на кнопку личный кабинет
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a')
        assert 'Профиль' in element.text
