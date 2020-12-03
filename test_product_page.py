from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


@pytest.mark.basket_guest
class TestGuestAddToBasketFromProductPage():
	@pytest.mark.need_review
	def test_guest_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
		page = ProductPage(browser, link)
		page.open()
		page.adding_to_basket_works_correctly()

	@pytest.mark.need_review
	def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
		page = ProductPage(browser, link)
		page.open()	
		page.go_to_basket_page()
		basket_page = BasketPage(browser, browser.current_url)
		basket_page.should_be_empty_basket()

	@pytest.mark.xfail
	def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
		page = ProductPage(browser, link)
		page.open()
		page.user_can_add_product_to_basket()
		page.should_not_be_success_message()

	def test_guest_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()

	@pytest.mark.xfail
	def test_message_disappeared_after_adding_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
		page = ProductPage(browser, link)
		page.open()
		page.user_can_add_product_to_basket()
		page.success_message_should_disappear()


@pytest.mark.login_guest
class TestLoginFromProductPage():
	@pytest.mark.need_review
	def test_guest_can_go_to_login_page_from_product_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
		page = ProductPage(browser, link)
		page.open()
		page.go_to_login_page()
		login_page = LoginPage(browser, browser.current_url)
		login_page.should_be_login_page()

	def test_guest_should_see_login_link_on_product_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
		page = ProductPage(browser, link)
		page.open()
		page.should_be_login_link()


@pytest.mark.basket_user
class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse="True")
	def setup(self, browser):
		login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
		login_page=LoginPage(browser, login_link)
		login_page.open()
		login_page.register_new_user((str(time.time()) + "@fakemail.org"), "vvv444fff")
		login_page.should_be_authorized_user()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
		page = ProductPage(browser, link)
		page.open()
		page.adding_to_basket_works_correctly()

	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()

