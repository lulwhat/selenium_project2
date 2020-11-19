from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo_number', \
	[pytest.param(i, marks=pytest.mark.xfail(i==7, reason='bugged promo')) \
	 for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_number):
	link = f"http://selenium1py.pythonanywhere.com\
	/catalogue/coders-at-work_207/?promo=offer{promo_number}"
	page = ProductPage(browser, link)
	page.open()
	page.product_page_works_correctly()