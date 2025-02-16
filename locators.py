from selenium.webdriver.common.by import By

class Locators:
    TEXT_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[1]/div/div/input') # локатор поля Имя
    TEXT_EMAIL_INPUT = (By.XPATH, "/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input")  # локатор поля email
    TEXT_PASSWORD_INPUT = (By.XPATH, "/html/body/div/div/main/div/div/div/ul/li[3]/div/div/input")  # локатор поля пароль (By.XPATH, "//input_container[@value= 'GoodLife']")

    BUTTON_REGISTER = (By.XPATH, "/html/body/div/div/main/div/div/p[1]/a")  # кнопка зарегистрироваться
    BUTTON_ENTER = (By.XPATH,"/html/body/div/div/main/div/div/p/a") # кнопка войти в форме регистрации /html/body/div/div/main/div/div/p/a  /html/body/div/div/main/div/form/button
    BUTTON_ENTER_PASSWORD_RECOVERY = (By.XPATH, "/html/body/div/div/main/div/div/p/a") # кнопка войти в форме восстановления пароля
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "/html/body/div/div/header/nav/a/p") #кнопка личный кабинет
    BUTTON_RECOVER_PASSWORD = (By.XPATH, "/html/body/div/div/main/div/div/p/a") # кнопка восстановить пароль (By.LINK_TEXT, "Восстановить пароль")
    BUTTON_DESIGNER = (By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p") # кнопка Конструктор
    BUTTON_STELLAR_BURGERS = (By.XPATH, "/html/body/div/div/header/nav/div/a") # логотип stellar burgers
    BUTTON_EXIT = (By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button") # кнопка Выход в форме личного кабинета
    CHAPTER_ROLLS = (By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[1]/span') # кнопка Булки
    #CHAPTER_ROLLS = (By.XPATH, "//span[text()='Булки']")
    CHAPTER_SAUCES = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]/span")   # кнопка соусы
    CHAPTER_FILLINGS = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]/span")  # кнопка Начинки


