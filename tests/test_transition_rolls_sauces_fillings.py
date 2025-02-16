from selenium.webdriver.common.by import By
from confest import driver


# проверяем раздел Конструктор
class TestTransitionRollsSaucesFillings:
    def test_transition_rolls(self,driver):
        # нажимаем на кнопку Булки
        driver.find_element_by_xpath(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span').click()
        transition_rolls = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]')
        assert 'Флюоресцентная булка' in transition_rolls.text

    def test_transition_sauces(self, driver):
        # нажимаем на кнопку Соусы
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()
        transition_sauces = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[1]/p')
        assert 'Соус Spicy-X' in transition_sauces

    def test_transition_fillings(self, driver):
        # нажимаем на кнопку Начинки
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span').click()
        transition_fillings = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[1]/img')
        assert 'Мясо бессмертных моллюсков Protostomia' in transition_fillings
