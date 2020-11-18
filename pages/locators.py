from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")

class ProductPageLocators():
	PRODUCT_GALLERY = (By.CSS_SELECTOR, "#product_gallery")
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")