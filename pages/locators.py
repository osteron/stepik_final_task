from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_EMAIL = (By.NAME, 'login-username')
    LOGIN_PASSWORD = (By.NAME, 'login-password')

    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.NAME, 'registration-email')
    REGISTER_PASSWORD = (By.NAME, 'registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.NAME, 'registration-password2')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    ALERT_ADDED_TO_BASKET = (By.CLASS_NAME, 'alert-success')
    ALERT_BOOK_TITLE = (By.CSS_SELECTOR, '.alertinner > strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main > h1')
    TOTAL_PRICE_BASKET = (By.CSS_SELECTOR, '.alertinner > p > strong')
