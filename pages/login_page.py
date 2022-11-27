from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, 'No URL of the current page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'No login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM), 'No registration form on the page'

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.USER_EMAIL)
        user_email.send_keys(email)

        user_pass = self.browser.find_element(*LoginPageLocators.USER_PASS)
        user_pass.send_keys(password)

        user_pass_repeat = self.browser.find_element(*LoginPageLocators.USER_PASS_REPEAT)
        user_pass_repeat.send_keys(password)

        registr_btn = self.browser.find_element(*LoginPageLocators.REGISTR_BTN)
        registr_btn.click()



