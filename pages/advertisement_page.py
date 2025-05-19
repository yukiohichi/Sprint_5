from selenium.webdriver.support.ui import WebDriverWait
from locators.advertisement_locators import AdvertisementLocators
from selenium.webdriver.support import expected_conditions

class AdvertisementPage:
    def __init__(self, driver):
        self.driver = driver

    def click_create_ad_button(self):
        locator = AdvertisementLocators.CREATE_AD_BUTTON
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        ).click()

    def wait_to_creation_page(self):
        WebDriverWait(self.driver, 10).until(
        expected_conditions.url_to_be("https://qa-desk.stand.praktikum-services.ru/create-lisiting")
    )

    def select_category(self):
        self.driver.find_element(*AdvertisementLocators.CATEGORY_MENU).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AdvertisementLocators.CATEGORY_TYPE_BUTTON)
        )

        self.driver.find_element(*AdvertisementLocators.CATEGORY_TYPE_BUTTON).click()

    def select_city(self):
        elements = self.driver.find_elements(*AdvertisementLocators.CITY_MENU)
        elements[1].click()

        self.driver.find_element(*AdvertisementLocators.CITY_TYPE_BUTTON).click()

    def click_product_state(self):
        self.driver.find_element(*AdvertisementLocators.PRODUCT_STATE).click()

    def find_text_ad(self):
        return self.driver.find_element(*AdvertisementLocators.TEXT_AD).is_displayed()



    def enter_description(self, text):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AdvertisementLocators.DESCRIPTION_INPUT)
        )
        self.driver.find_element(*AdvertisementLocators.DESCRIPTION_INPUT).send_keys(text)

    def enter_price(self, price):
        self.driver.find_element(*AdvertisementLocators.PRICE_INPUT).send_keys(price)


    def wait_for_create_ad_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(AdvertisementLocators.CREATE_AD_BUTTON))

    def wait_and_enter_name_input(self, name):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(AdvertisementLocators.NAME_INPUT))
        self.driver.find_element(*AdvertisementLocators.NAME_INPUT).send_keys(name)

    def get_ad_product(self):
        title = self.driver.find_element(*AdvertisementLocators.TITLE_AD)
        return title.text

    def scroll_to_publish_button(self):
        element = self.driver.find_element(*AdvertisementLocators.PUBLISH_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def publish_ad_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AdvertisementLocators.PUBLISH_BUTTON)
        )
        self.driver.find_element(*AdvertisementLocators.PUBLISH_BUTTON).click()

    def wait_for_title_ad(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(AdvertisementLocators.TITLE_AD)
        )

