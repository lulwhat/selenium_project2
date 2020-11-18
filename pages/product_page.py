from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def should_be_product_page(self):
		self.should_be_product_url()
		self.should_be_product_gallery()
		self.user_can_add_product_to_basket()

	def should_be_product_url(self):
		assert 'catalogue' in self.browser.current_url, "Not a product URL"

	def should_be_product_gallery(self):
		assert self.is_element_present(*ProductPageLocators.PRODUCT_GALLERY), \
			"Product gallery is not presented"

	def user_can_add_product_to_basket(self):
		add_to_basket_button = \
			self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		add_to_basket_button.click()
		self.solve_quiz_and_get_code()