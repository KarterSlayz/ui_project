from selenium.webdriver.common.by import By

fname_field_loc = (By.ID, 'firstname')
lname_field_loc = (By.ID, 'lastname')
email_field_loc = (By.ID, 'email_address')
pass_field_loc = (By.ID, 'password')
confirm_pass_field_loc = (By.ID, 'password-confirmation')
create_button_loc = (By.CSS_SELECTOR, '#form-validate > div > div.primary > button')
info_loc = (By.CLASS_NAME, 'box-content')
password_error_loc = (By.ID, 'password-error')
err_empty_field_fname = (By.ID, 'firstname-error')
page_message_loc = (By.XPATH, '//*[@id="maincontent"]/div[1]')
