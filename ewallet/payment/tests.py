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
    

    
    def test_payment_1(self):
        self.browser.get(self.live_server_url)
        link = self.browser.find_element_by_link_text('Register')
        link.click()
        user=self.browser.find_element_by_name("username")
        password1=self.browser.find_element_by_name("password1")
        password2=self.browser.find_element_by_name("password2")
        user.clear()
        user_text1=uuid.uuid4().hex
        pass_text1=uuid.uuid4().hex
        user.send_keys(user_text1)
        password1.clear()
        password1.send_keys(pass_text1)
        password2.clear()
        password2.send_keys(pass_text1)
        submit_button= self.browser.find_element_by_css_selector("input[type='submit']")
        submit_button.click()

        #add money
        bal=int(self.browser.find_element_by_name("balance").text)
        num=random.randint(0,100000000)
        dep_field=self.browser.find_element_by_name("dep_amt")
        dep_field.clear()
        dep_field.send_keys(str(num))
        submit_button= self.browser.find_element_by_css_selector("input[value='Deposit']")
        submit_button.click()
        bal_new=int(self.browser.find_element_by_name("balance").text)

        self.assertEquals(bal+num,bal_new)

        #valid withdrawal
        bal=int(self.browser.find_element_by_name("balance").text)
        num=random.randint(0,bal)
        wit_field=self.browser.find_element_by_name("wit_amt")
        wit_field.clear()
        wit_field.send_keys(str(num))
        submit_button= self.browser.find_element_by_css_selector("input[value='Withdraw']")
        submit_button.click()
        bal_new=int(self.browser.find_element_by_name("balance").text)

        self.assertEquals(bal-num,bal_new)

        #invalid withdrawal
        bal=int(self.browser.find_element_by_name("balance").text)
        num=random.randint(bal,100000000000000000)
        wit_field=self.browser.find_element_by_name("wit_amt")
        wit_field.clear()
        wit_field.send_keys(str(num))
        submit_button= self.browser.find_element_by_css_selector("input[value='Withdraw']")
        submit_button.click()
        bal_new=int(self.browser.find_element_by_name("balance").text)

        bal_1=bal_new

        self.assertEquals(bal,bal_new)

        link = self.browser.find_element_by_link_text('Logout')
        link.click()

        print("Deposit and Withdraw testing complete")


        link = self.browser.find_element_by_link_text('Register')
        link.click()

        #creates second user
        user=self.browser.find_element_by_name("username")
        password1=self.browser.find_element_by_name("password1")
        password2=self.browser.find_element_by_name("password2")
        user.clear()
        user_text2=uuid.uuid4().hex
        pass_text2=uuid.uuid4().hex
        user.send_keys(user_text2)
        password1.clear()
        password1.send_keys(pass_text2)
        password2.clear()
        password2.send_keys(pass_text2)
        submit_button= self.browser.find_element_by_css_selector("input[type='submit']")
        submit_button.click()

        #valid withdrawal
        bal=int(self.browser.find_element_by_name("balance").text)
        num=random.randint(0,100000000)
        dep_field=self.browser.find_element_by_name("dep_amt")
        dep_field.clear()
        dep_field.send_keys(str(num))
        submit_button= self.browser.find_element_by_css_selector("input[value='Deposit']")
        submit_button.click()
        bal_new=int(self.browser.find_element_by_name("balance").text)

        self.assertEquals(bal+num,bal_new)

        #valid transaction
        bal=int(self.browser.find_element_by_name("balance").text)
        num=random.randint(bal,100000000000)
        wit_field=self.browser.find_element_by_name("trans_amt")
        wit_field.clear()
        wit_field.send_keys(str(num))
        recep=self.browser.find_element_by_name("recipient")
        recep.clear()
        recep.send_keys(user_text1)
        submit_button= self.browser.find_element_by_css_selector("input[value='Transfer']")
        submit_button.click()
        bal_new=int(self.browser.find_element_by_name("balance").text)

        self.assertEquals(bal,bal_new)

        #invalid transfer
        bal=int(self.browser.find_element_by_name("balance").text)
        num=random.randint(0,bal)
        wit_field=self.browser.find_element_by_name("trans_amt")
        wit_field.clear()
        wit_field.send_keys(str(num))
        recep=self.browser.find_element_by_name("recipient")
        recep.clear()
        recep.send_keys(user_text1)
        submit_button= self.browser.find_element_by_css_selector("input[value='Transfer']")
        submit_button.click()
        bal_new=int(self.browser.find_element_by_name("balance").text)

        self.assertEquals(bal-num,bal_new)


        link = self.browser.find_element_by_link_text('Logout')
        link.click()

        user=self.browser.find_element_by_name("username")
        password=self.browser.find_element_by_name("password")
        

        #check other account

        user.clear()
        user.send_keys(user_text1)
        password.clear()
        password.send_keys(pass_text1)

        submit_button= self.browser.find_element_by_css_selector("input[type='submit']")
        submit_button.click()

        bal_new=int(self.browser.find_element_by_name("balance").text)

        self.assertEquals(bal_1+num,bal_new)



    def test_registration_failure(self):
        self.browser.get(self.live_server_url)
        link = self.browser.find_element_by_link_text('Register')
        link.click()
        user=self.browser.find_element_by_name("username")
        password1=self.browser.find_element_by_name("password1")
        password2=self.browser.find_element_by_name("password2")
        user.clear()
        user_text=uuid.uuid4().hex
        pass_text=uuid.uuid4().hex
        user.send_keys(user_text)
        password1.clear()
        password1.send_keys(pass_text+uuid.uuid4().hex)
        password2.clear()
        password2.send_keys(pass_text)
        submit_button= self.browser.find_element_by_css_selector("input[type='submit']")
        submit_button.click()

        self.assertNotEquals("Welcome , "+user_text,self.browser.find_element_by_tag_name("h1").text)


    def test_registration_success_login(self):
        self.browser.get(self.live_server_url)
        link = self.browser.find_element_by_link_text('Register')
        link.click()
        user=self.browser.find_element_by_name("username")
        password1=self.browser.find_element_by_name("password1")
        password2=self.browser.find_element_by_name("password2")
        user.clear()
        user_text=uuid.uuid4().hex
        pass_text=uuid.uuid4().hex
        user.send_keys(user_text)
        password1.clear()
        password1.send_keys(pass_text)
        password2.clear()
        password2.send_keys(pass_text)
        submit_button= self.browser.find_element_by_css_selector("input[type='submit']")
        submit_button.click()

        self.assertEquals("Welcome , "+user_text,self.browser.find_element_by_tag_name("h1").text)


        link = self.browser.find_element_by_link_text('Logout')
        link.click()

        user=self.browser.find_element_by_name("username")
        password=self.browser.find_element_by_name("password")
        



        user.clear()
        user.send_keys(user_text)
        password.clear()
        password.send_keys(pass_text)

        submit_button= self.browser.find_element_by_css_selector("input[type='submit']")
        submit_button.click()

        self.assertEquals("Welcome , "+user_text,self.browser.find_element_by_tag_name("h1").text)






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

        