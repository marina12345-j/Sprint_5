from selenium.webdriver.common.by import By


# проверяем раздел Конструктор
class TestTransitionRollsSaucesFillings:
    def test_transition_rolls(self,driver):
        # нажимаем на кнопку Булки (секция)
        section_rolls = driver.find_element_by_xpath(By.XPATH, "//span[text() = 'Булки' and @class = 'text text_type_main-default']").click()
        transition_rolls = driver.find_element(By.XPATH, "//h2[text() = 'Булки' and @class = 'text text_type_main-medium mb-6 mt-10")
        assert section_rolls.text == 'Булки' and transition_rolls == 'Булки'

    def test_transition_sauces(self, driver):
        # нажимаем на кнопку Соусы (секция)
        section_souses = driver.find_element(By.XPATH, "//span[text() = 'Соусы' and @class = 'text text_type_main-default']").click()

        transition_sauces = driver.find_element(By.XPATH, "//h2[text() = 'Соусы' and @class = 'text text_type_main-medium mb-6 mt-10']")
        assert section_souses.text == 'Соусы' and transition_sauces.text == 'Соусы'

    def test_transition_fillings(self, driver):
        # нажимаем на кнопку Начинки (секция)
        section_fillings = driver.find_element(By.XPATH, "//span[text() = 'Начинки' and @class = 'text text_type_main-default']").click()
        transition_fillings = driver.find_element(By.XPATH, "//h2[text() = 'Начинки' and @class = 'text text_type_main-medium mb-6 mt-10']")
        assert section_fillings.text == 'Начинки' and transition_fillings.text == 'Начинки'



