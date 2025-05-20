from selenium.webdriver.common.by import By


class RegistrationLocators:
    AUTH_BUTTON = (By.XPATH, '//button[text()="Вход и регистрация"]')
    ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Нет аккаунта"]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[text()="Создать аккаунт"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    EXIT_BUTTON = (By.XPATH, '//button[text()="Выйти"]')

    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Введите Email"]')
    PASS_INPUT = (By.XPATH, '//input[@placeholder="Пароль"]')
    PASS_CONFIRM_INPUT = (By.XPATH, '//input[@placeholder="Повторите пароль"]')

    USER_AVATAR = (By.XPATH, '//button[@class="circleSmall"]')
    PROFILE_TEXT = (By.XPATH, '//h1[text()="Мой профиль"]')
    AD_STATE_LIST = (By.XPATH,'//div[contains(@class, "profilePage")]//h1[text()="Мои объявления"]')

    USER_NAME = (By.XPATH, '//h3[text()="User."]')
    REGISTRATION_ERROR_TEXT = (By.XPATH, '//span[text()="Ошибка"]')

    EMAIL_ERROR_BORDER = (By.XPATH, "//input[@name='email']/parent::div[contains(@class, 'input_inputError')]")
    PASS_ERROR_BORDER = (By.XPATH, "//input[@name='password']/parent::div[contains(@class, 'input_inputError')]")
    CONFIRM_PASS_ERROR_BORDER = (By.XPATH, "//input[@name='submitPassword']/parent::div[contains(@class, 'input_inputError')]")
