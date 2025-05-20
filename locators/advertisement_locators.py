from selenium.webdriver.common.by import By

class AdvertisementLocators:
    CREATE_AD_BUTTON = (By.XPATH, '//button[starts-with(@class, "buttonPrimary")]')
    PUBLISH_BUTTON = (By.XPATH, '//button[text()="Опубликовать"]')

    NAME_INPUT = (By.XPATH, '//input[@placeholder="Название"]')
    PRICE_INPUT = (By.NAME, 'price')

    CATEGORY_MENU = (By.XPATH, '//div[starts-with(@class, "createListing_inputRow")]//button[starts-with(@class, "dropDownMenu_arrowDown")]')
    CATEGORY_TYPE_BUTTON = (By.XPATH, '//span[text()="Книги"]/parent::button[starts-with(@class, "dropDownMenu_btn")]')

    CITY_MENU = (By.XPATH, '//div[starts-with(@class, "dropDownMenu_dropMenu")]//button[starts-with(@class, "dropDownMenu_arrowDown")]')
    CITY_TYPE_BUTTON = (By.XPATH, '//button/span[text()="Новосибирск"]')

    PRODUCT_STATE = (By.XPATH, '//label[text()="Б/У"]')
    TEXT_AD = (By.XPATH, '//h1[text()="Чтобы разместить объявление, авторизуйтесь"]')
    DESCRIPTION_INPUT = (By.XPATH, '//div[contains(@class, "textarea_inputDefault")]//textarea[@name="description"]')

    TITLE_AD = (By.XPATH, '//div[@class="about"]//h2[@class="h2"]')



