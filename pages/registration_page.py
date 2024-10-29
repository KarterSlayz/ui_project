from pages.base_page import BasePage
from pages.locators import registration_locator as loc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage(BasePage):
    page_url = '/customer/account/create/'

    def fill_create_akk_form(self,
                             fname,
                             lname,
                             email,
                             passwd,
                             confpasswd
                             ):
        name_field = self.find(loc.fname_field_loc)
        lname_field = self.find(loc.lname_field_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.pass_field_loc)
        conf_password_field = self.find(loc.confirm_pass_field_loc)
        name_field.send_keys(fname)
        lname_field.send_keys(lname)
        email_field.send_keys(email)
        password_field.send_keys(passwd)
        conf_password_field.send_keys(confpasswd)
        create_button = self.find(loc.create_button_loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", create_button)
        create_button.click()
        page_message = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(loc.page_message_loc)
        )
        assert page_message.text == 'Thank you for registering with Main Website Store.'

    def data_verification(self,
                          fname,
                          lname,
                          email,
                          ):
        info_akk = self.find(loc.info_loc)
        assert fname, lname and email in info_akk.text

    def rules_passwd(self, passwd, text):
        invalid_passwd = self.find(loc.pass_field_loc)
        invalid_passwd.send_keys(passwd)
        err_passwd = self.find(loc.password_error_loc)
        assert err_passwd.text == text

    def create_with_empty_field(self, text):
        create_button = self.find(loc.create_button_loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", create_button)
        create_button.click()
        err_empty_field = self.find(loc.err_empty_field_fname)
        assert err_empty_field.text == text
