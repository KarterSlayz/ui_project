import pytest


@pytest.mark.smoke
def test_title_page(sale_page):
    sale_page.open_page()
    sale_page.page_title()


@pytest.mark.button_to_women_sale
def test_transition_to_woman_sale(sale_page):
    sale_page.open_page()
    sale_page.transition_to_woman_sale()


@pytest.mark.sale_off
def test_text_sale_off(sale_page):
    sale_page.open_page()
    sale_page.sale_off()
