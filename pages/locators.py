from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_EMAIL = (By.NAME, 'login-username')
    LOGIN_PASSWORD = (By.NAME, 'login-password')
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')

    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.NAME, 'registration-email')
    REGISTER_PASSWORD = (By.NAME, 'registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.NAME, 'registration-password2')
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    ALERT_ADDED_TO_BASKET = (By.CSS_SELECTOR, '#messages > .alert')
    ALERT_BOOK_TITLE = (By.CSS_SELECTOR, '.alertinner > strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main > h1')
    TOTAL_PRICE_BASKET = (By.CSS_SELECTOR, '.alertinner > p > strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini > span > a')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner')
    USER_ICON = (By.CLASS_NAME, "icon-user")
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_link')


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
