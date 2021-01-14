""" Functional test for registration and login user behavior """

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestUserBehavior(StaticLiveServerTestCase):
    """Functional test for the login and registeration behiavor"""

    def setUp(self):
        """Setting up tests variables and config"""
        self.browser = webdriver.Chrome(
            "purbeurre/users/tests/chromedriver", options=chrome_options
        )
        self.username = "Gaetan"
        self.email = "hello@gaetangr.me"
        self.password = "you-will-never-guess"

    def tearDown(self):
        self.browser.close()

    def test_if_user_can_register_and_login(self):
        """User should be able to register, login and then access their profil page"""

        # Accessing live server
        self.browser.get(self.live_server_url)

        # Accesing registeration page and filling out information
        self.browser.find_element_by_css_selector("#sign-up-link").click()
        self.browser.find_element_by_css_selector("#id_username").send_keys(
            self.username
        )
        self.browser.find_element_by_css_selector("#id_password1").send_keys(
            self.password
        )
        self.browser.find_element_by_css_selector("#id_password2").send_keys(
            self.password
        )
        self.browser.find_element_by_css_selector("#id_email").send_keys(self.email)
        self.browser.find_element_by_css_selector("#button-submit").click()

        # Loging in
        self.browser.find_element_by_css_selector("#id_username").send_keys(
            self.username
        )
        self.browser.find_element_by_css_selector("#id_password").send_keys(
            self.password
        )
        self.browser.find_element_by_css_selector("#button-submit").click()

        # Accessing user profile
        self.browser.find_element_by_css_selector("#user-detail").click()
