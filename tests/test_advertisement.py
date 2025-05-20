from pages.advertisement_page import AdvertisementPage
from pages.registration_page import RegistrationPage

def test_create_ad_unauthorized_user(driver):
    page_user = RegistrationPage(driver)
    page_ad = AdvertisementPage(driver)

    page_user.wait_for_auth_button()

    page_ad.click_create_ad_button()
    page_user.wait_for_account_button()

    assert page_ad.find_text_ad(), 'Ожидаемый текст не найден'


def test_create_ad(driver, user, name, text_description, price):
    email_user, password_user = user

    page_ad = AdvertisementPage(driver)
    page_user = RegistrationPage(driver)

    page_user.login_user(email_user, password_user)

    page_ad.wait_for_create_ad_button()
    page_ad.click_create_ad_button()
    page_ad.wait_to_creation_page()

    page_ad.wait_and_enter_name_input(name)
    page_ad.select_category()
    page_ad.click_product_state()
    page_ad.scroll_to_publish_button()
    page_ad.select_city()
    page_ad.enter_description(text_description)
    page_ad.enter_price(price)

    page_ad.publish_ad_button()

    page_user.wait_for_user_avatar()
    page_user.scroll_element_user_avatar_button()

    page_user.go_to_user_profile()
    page_ad.wait_for_title_ad()

    ad_title = page_ad.get_ad_product()

    assert name == ad_title, f"Название объявления '{ad_title}' не совпадает с ожидаемым '{name}'"





