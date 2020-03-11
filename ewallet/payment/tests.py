from django.test import TestCase


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from payment.models import Transaction, Wallet

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

import time
import uuid
import random


class TestProject(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'./geckodriver')

    def tearDown(self):
        self.browser.close()


    def test_registration_screen_open(self):
        self.browser.get(self.live_server_url)
        link = self.browser.find_element_by_link_text('Register')
        link.click()

        self.assertEquals(self.browser.find_element_by_tag_name("h1").text ,"Registration")
    



















        




'''
    def test_login_screen(self):
        self.browser.get(self.live_server_url)
        user=self.browser.find_element_by_name("username")
        password=self.browser.find_element_by_name("password")
        

        user.clear()
        user.send_keys("user6")
        password.clear()
        password.send_keys("password1234567")
        password.send_keys(Keys.RETURN)

        self.assertIn("Welcome",self.browser.page_source)
'''

        