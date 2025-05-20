from pages.registration_page import RegistrationPage


def test_registration_user(driver,email,password):

    page = RegistrationPage(driver)

    page.click_auth_button()
    page.wait_for_account_button()

    page.click_account_button()
    page.wait_for_email()
    page.enter_email(email)
    page.enter_password(password)
    page.enter_confirm_password(password)
    page.click_register_button()
    page.wait_for_user_avatar()

    assert (page.find_user_name()
            and page.find_user_avatar()), \
        "Авторизация не пройдена"


def test_registration_user_bad_email(driver):

    page = RegistrationPage(driver)
    page.click_auth_button()
    page.wait_for_account_button()
    page.click_account_button()
    page.wait_for_email()
    page.enter_email('aaa')
    page.click_register_button()
    page.wait_for_error_text()

    assert page.find_error_text(), "Ошибка не отображается под полем Email"
    assert page.is_email_border_red(), "Граница поля Email не подсвечена красным"
    assert page.is_password_border_red(), "Граница поля Пароль не подсвечена красным"
    assert page.is_confirm_password_border_red(), "Граница поля Повторите пароль не подсвечена красным"


def test_registration_existing_user(driver, user):
    email_user, password_user = user
    page = RegistrationPage(driver)

    page.wait_for_auth_button()
    page.click_auth_button()

    page.wait_for_account_button()
    page.click_account_button()

    page.wait_for_email()
    page.enter_email(email_user)
    page.enter_password(password_user)
    page.enter_confirm_password(password_user)
    page.click_register_button()
    page.wait_for_error_text()

    assert page.find_error_text(), "Ошибка не отображается под полем Email"
    assert page.is_email_border_red(), "Граница поля Email не подсвечена красным"
    assert page.is_password_border_red(), "Граница поля Пароль не подсвечена красным"
    assert page.is_confirm_password_border_red(), "Граница поля Повторите пароль не подсвечена красным"


def test_auth_user(driver, user):
    email_user, password_user = user
    page = RegistrationPage(driver)

    page.wait_for_auth_button()
    page.click_auth_button()

    page.wait_for_email()
    page.enter_email(email_user)
    page.enter_password(password_user)
    page.click_login_button()
    page.wait_for_user_avatar()

    assert (page.find_user_name()
            and page.find_user_avatar()), \
        "Авторизация не пройдена"


def test_existing_user(driver, user):
    email_user, password_user = user
    page = RegistrationPage(driver)

    page.wait_for_auth_button()
    page.click_auth_button()

    page.wait_for_email()
    page.enter_email(email_user)
    page.enter_password(password_user)
    page.click_login_button()
    page.wait_for_user_avatar()

    page.click_exit_button()
    page.wait_for_auth_button()

    assert page.find_auth_button(), "Кнопка 'Вход и регистрация' не отображается"