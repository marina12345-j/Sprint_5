from locators import Locators


# проверяем раздел Конструктор
class TestTransitionRollsSaucesFillings:
    def test_transition_rolls(self,driver):
        # нажимаем на кнопку Булки (секция)
        section_rolls = driver.find_element_by_xpath(Locators.CHAPTER_ROLLS).click()
        transition_rolls = driver.find_element(Locators.TITTLE_ROLLS)
        assert section_rolls.text == 'Булки' and transition_rolls.text == 'Булки'

    def test_transition_sauces(self, driver):
        # нажимаем на кнопку Соусы (секция)
        section_souses = driver.find_element(Locators.CHAPTER_SAUCES).click()

        transition_sauces = driver.find_element(Locators.TITTLE_SAUCES)
        assert section_souses.text == 'Соусы' and transition_sauces.text == 'Соусы'

    def test_transition_fillings(self, driver):
        # нажимаем на кнопку Начинки (секция)
        section_fillings = driver.find_element(Locators.CHAPTER_FILLINGS).click()
        transition_fillings = driver.find_element(Locators.TITTLE_FILLINGS)
        assert section_fillings.text == 'Начинки' and transition_fillings.text == 'Начинки'
