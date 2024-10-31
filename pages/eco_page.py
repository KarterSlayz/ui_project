from pages.base_page import BasePage
from pages.locators import eco_locator as loc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class EcoPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def adding_first_product_to_cart(self):
        actions = ActionChains(self.driver)
        item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.product_item_loc)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", item)
        actions.move_to_element(item).perform()
        size = self.find(loc.product_size_loc)
        size.click()
        color = self.find(loc.product_color_loc)
        color.click()
        add_cart_button = self.find(loc.button_add_cart_loc)
        add_cart_button.click()
        return item

    def check_name_item_in_page_message(self):
        page_message = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.page_message_loc)
        )
        assert self.adding_first_product_to_cart().text in page_message.text

    def check_adding_item_in_cart(self):
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.cart_button_loc)
        )
        cart_button.click()
        item_in_cart = self.find(loc.item_in_cart_loc)
        assert self.adding_first_product_to_cart().text == item_in_cart.text

    def switching_pages(self):
        current_url = self.driver.current_url
        switch = self.find(loc.switch_gape_loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", switch)
        switch.click()
        new_url = self.driver.current_url
        assert new_url != current_url

    def sorted_items_in_page_by_price(self):
        sorted_dropdown = self.find(loc.sorted_items_loc)
        dropdown = Select(sorted_dropdown)
        dropdown.select_by_value('price')
        price_first_item = self.find(loc.price_item).get_attribute('data-price-amount')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.product_item_loc)
        )
        action_sorted = self.find(loc.action_sorted)
        action_sorted.click()
        new_price_first_item = self.find(loc.new_price_item).get_attribute('data-price-amount')
        assert price_first_item < new_price_first_item
