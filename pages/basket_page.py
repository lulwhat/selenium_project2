from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	def should_be_empty_basket(self):
		message = self.browser.find_element(
			*BasketPageLocators.EMPTY_BASKET_MESSAGE
		)
		assert message.text == "Your basket is empty. Continue shopping", \
			"Empty basket message should be presented"