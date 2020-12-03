from selenium.webdriver.common.by import By


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
	REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.CSS_SELECTOR, "[value='Register']")
	LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
	LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
	LOGIN_BUTTON = (By.CSS_SELECTOR, "[value='Log In']")
	

class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")

class BasketPageLocators():
	ADDED_PRODUCT_NAME = (By.CSS_SELECTOR ,".alert-safe:nth-child(1) strong")
	BASKET_TOTAL = (By.CSS_SELECTOR ,".alert-safe:nth-child(3) strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR ,".alert")
	EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default:nth-child(1)")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")