from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest

# testing promo codes
@pytest.mark.parametrize('promo_number', \
	[pytest.param(i, marks=pytest.mark.xfail(i==7, reason='bugged promo')) \
	 for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_number):
	link = f"http://selenium1py.pythonanywhere.com\
	/catalogue/coders-at-work_207/?promo=offer{promo_number}"
	page = ProductPage(browser, link)
	page.open()
	page.adding_to_basket_works_correctly()

# negative tests
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	page = ProductPage(browser, link)
	page.open()
	page.user_can_add_product_to_basket()
	page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	page = ProductPage(browser, link)
	page.open()
	page.user_can_add_product_to_basket()
	page.success_message_should_disappear()

# tests after adding common methods to BasePage
def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()
	page = LoginPage(browser, browser.current_url)
	page.should_be_login_page()