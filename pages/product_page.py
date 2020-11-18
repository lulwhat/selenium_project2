from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators


class ProductPage(BasePage):
	def product_page_works_correctly(self):
		self.user_can_add_product_to_basket()
		self.added_product_name_is_correct()
		self.basket_total_is_correct()

	def user_can_add_product_to_basket(self):
		self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		add_to_basket_button = \
			self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		add_to_basket_button.click()
		self.solve_quiz_and_get_code()

	def added_product_name_is_correct(self):
		assert self.browser.find_element(*BasketPageLocators.ADDED_PRODUCT_NAME).text \
			== self.product_name, "Added product name doesn't match with name in the basket"

	def basket_total_is_correct(self):
		assert self.browser.find_element(*BasketPageLocators.BASKET_TOTAL).text \
			== self.product_price, "Added product price doesn't match with basket total"		