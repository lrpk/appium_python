from .page import Page
from utils.android_utils import email_field_locator, pas_field_locator, login_btn_locator, banner_locator


class LoginPage(Page):

    def login_btn(self):
        self.click_element(login_btn_locator)

    def input_email(self, email):
        email_field = self.find_element(email_field_locator)
        email_field.send_keys(email)

    def input_password(self, password):
        password_field = self.find_element(pas_field_locator)
        password_field.send_keys(password)

    def check_for_banner(self):
        return not self.banner_displayed(banner_locator)


