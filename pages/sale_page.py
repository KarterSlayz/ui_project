from pages.base_page import BasePage
from pages.locators import sale_locator as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def page_title(self):
        title = self.find(loc.title_page_loc)
        assert title.text == 'Sale'

    def transition_to_woman_sale(self):
        button = self.find(loc.woman_deals_button_loc)
        button.click()
        title_page = self.find(loc.title_page_loc)
        assert title_page.text == 'Women Sale'

    def sale_off(self):
        sale_text = self.find(loc.sale_off_loc)
        assert sale_text.text == 'Every $200-plus purchase!'
