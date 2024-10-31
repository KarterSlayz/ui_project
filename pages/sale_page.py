from pages.base_page import BasePage
from pages.locators import sale_locator as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def page_title(self, text):
        title = self.find(loc.title_page_loc)
        assert title.text == text

    def transition_to_woman_sale(self, text):
        button = self.find(loc.woman_deals_button_loc)
        button.click()
        title_page = self.find(loc.title_page_loc)
        assert title_page.text == text

    def sale_off(self, text):
        sale_text = self.find(loc.sale_off_loc)
        assert sale_text.text == text
