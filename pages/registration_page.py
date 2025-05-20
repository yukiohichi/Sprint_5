from selenium.webdriver.support.ui import WebDriverWait
from locators.registration_locators import RegistrationLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def click_auth_button(self):
        self.driver.find_element(*RegistrationLocators.AUTH_BUTTON).click()

    def click_account_button(self):
        self.driver.find_element(*RegistrationLocators.ACCOUNT_BUTTON).click()

    def click_register_button(self):
        self.driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON).click()

    def click_exit_button(self):
        self.driver.find_element(*RegistrationLocators.EXIT_BUTTON).click()

    def click_login_button(self):
        self.driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()

    def click_user_avatar_button(self):
        self.driver.find_element(*RegistrationLocators.USER_AVATAR).click()


    def enter_email(self, email):
        self.driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*RegistrationLocators.PASS_INPUT).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(*RegistrationLocators.PASS_CONFIRM_INPUT).send_keys(password)


    def find_user_avatar(self):
        return self.driver.find_element(*RegistrationLocators.USER_AVATAR).is_displayed()

    def find_user_name(self):
        return self.driver.find_element(*RegistrationLocators.USER_NAME).is_displayed()

    def find_error_text(self):
        return self.driver.find_element(*RegistrationLocators.REGISTRATION_ERROR_TEXT).is_displayed()

    def find_auth_button(self):
        return self.driver.find_element(*RegistrationLocators.AUTH_BUTTON).is_displayed()

    def find_profile_text(self):
        return self.driver.find_element(*RegistrationLocators.PROFILE_TEXT).is_displayed()


    def get_border_color(self, locator):
        element = self.driver.find_element(*locator)
        return element.value_of_css_property("border-color")

    def is_email_border_red(self):
        color = self.get_border_color(RegistrationLocators.EMAIL_ERROR_BORDER)
        return color in ("rgb(255, 105, 114)", "rgba(255, 105, 114, 1)")

    def is_password_border_red(self):
        color = self.get_border_color(RegistrationLocators.PASS_ERROR_BORDER)
        return color in ("rgb(255, 105, 114)", "rgba(255, 105, 114, 1)")

    def is_confirm_password_border_red(self):
        color = self.get_border_color(RegistrationLocators.CONFIRM_PASS_ERROR_BORDER)
        return color in ("rgb(255, 105, 114)", "rgba(255, 105, 114, 1)")



    def wait_for_auth_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationLocators.AUTH_BUTTON))

    def wait_for_account_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationLocators.ACCOUNT_BUTTON))

    def wait_for_email(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT))

    def wait_for_user_avatar(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.USER_AVATAR))

    def wait_for_error_text(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(RegistrationLocators.REGISTRATION_ERROR_TEXT))

    def login_user(self, email, password):
        self.wait_for_auth_button()
        self.click_auth_button()
        self.wait_for_email()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_user_avatar()

    def scroll_element_user_avatar_button(self):
        profile_user = self.driver.find_element(*RegistrationLocators.USER_AVATAR)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", profile_user)

    def go_to_user_profile(self):
        avatar_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.USER_AVATAR)
        )

        ActionChains(self.driver).move_to_element(avatar_button).click().perform()