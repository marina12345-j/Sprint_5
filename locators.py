from selenium.webdriver.common.by import By

class Locators:
    TEXT_NAME_INPUT = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input") # локатор поля Имя
    TEXT_EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")  # локатор поля email
    TEXT_PASSWORD_INPUT = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")  # локатор поля пароль
    COD_FROM_EMAIL = (By.XPATH, "//label[text() = 'Ведите код из письма'/following-sibling::input") # поле Ведите код из письма
    HEADING_GO = (By.XPATH, "//h2[text() = 'Вход']")  # заголовок Вход в форме Вход

    BUTTON_LOG_IN_ACCOUNT = (By.XPATH, "//button[text() = 'Войти в аккаунт']") # Кнопка "Войти в аккаунт" на главной странице

    BUTTON_IN_GO = (By.XPATH, " //button[text() = 'Войти']") #кнопка Войти в форме Вход
    BUTTON_ENTER = (By.XPATH, "//a[text() = 'Войти']") # кнопка войти в форме восстановления пароля # кнопка войти в форме регистрации #кнопка вспомнили пароль? Войти


    BUTTON_REGISTER = (By.XPATH, "//button[text() = 'Зарегистрироваться']") # кнопка зарегистрироваться в форме регистрации
    BUTTON_REGISTER_NEW = (By.XPATH,  "//a[text() = 'Зарегистрироваться']")  # кнопка зарегистрироваться в форме Вход (вы новый пользователь?)

    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//a[@href = '/account']") #кнопка ЛИЧНЫЙ КАБИНЕТ

    BUTTON_RECOVER_PASSWORD = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # кнопка восстановить пароль (By.LINK_TEXT, "Восстановить пароль")
    BUTTON_RECOVER = (By.XPATH,"//button[text() = 'Восстановить']")  # кнопка Восстановить в поле Восстановление пароля

    BUTTON_DESIGNER = (By.XPATH, "//a[@class = 'AppHeader_header__link__3D_hX' and @href = '/']/p[text() = 'Конструктор']") # кнопка Конструктор
    BUTTON_STELLAR_BURGERS = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']/a[@href = '/']") # логотип stellar burgers
    BUTTON_EXIT = (By.XPATH, "//button[text() = 'Выход']") # кнопка Выход в форме личного кабинета

    CHAPTER_ROLLS = (By.XPATH, "//span[text() = 'Булки' and @class = 'text text_type_main-default']") # кнопка Булки
    TITTLE_ROLLS = (By.XPATH, "//h2[text() = 'Булки' and @class = 'text text_type_main-medium mb-6 mt-10']")  # Заголовок списка булок

    CHAPTER_SAUCES = (By.XPATH, "//span[text() = 'Соусы' and @class = 'text text_type_main-default']")   # кнопка соусы
    TITTLE_SAUCES = (By.XPATH, "//h2[text() = 'Соусы' and @class = 'text text_type_main-medium mb-6 mt-10']") # Заголовок списка соусы

    CHAPTER_FILLINGS = (By.XPATH, "//span[text() = 'Начинки' and @class = 'text text_type_main-default']")  # кнопка Начинки
    TITTLE_FILLINGS = (By.XPATH, "//h2[text() = 'Начинки' and @class = 'text text_type_main-medium mb-6 mt-10']") # Заголовок списка Начинки

    BUTTON_SAVE = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')  # кнопка Сохранить в форме восстановления

    BUTTON_PLACE_ON_ORDER = (By.XPATH, "//button[text() = 'Оформить заказ']") # кнопка оформить заказ
    TITTLE_ASSEMBLE_THE_BURGER = (By.XPATH, "//h1[text() = 'Соберите бургер' and @class = 'text text_type_main-large mb-5 mt-10']") # заголовок Соберите бургер

