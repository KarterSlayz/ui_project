from selenium.webdriver.common.by import By


product_item_loc = (By.CSS_SELECTOR, '.product-item:first-child .product-item-link')
product_size_loc = (By.XPATH, '//*[@id="option-label-size-143-item-171"]')
product_color_loc = (By.XPATH, '//*[@id="option-label-color-93-item-49"]')
button_add_cart_loc = (By.CSS_SELECTOR, "button.action.tocart")
cart_button_loc = (By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/a')
item_in_cart_loc = (By.XPATH, '//*[@id="mini-cart"]/li')
page_message_loc = (By.XPATH, '//*[@id="maincontent"]/div[2]/div[2]/div/div/div')
switch_gape_loc = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[4]/div[2]/ul/li[3]/a')
sorted_items_loc = (By.ID, 'sorter')
price_item = (By.XPATH, '//*[@id="product-price-718"]')
new_price_item = (By.XPATH, '//*[@id="product-price-94"]')
action_sorted = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[2]/div[4]/a')
