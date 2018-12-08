from selenium import webdriver
from selenium.webdriver.support.select import Select


class BankHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.username = self.driver.find_element_by_id('txtuId')
        self.password = self.driver.find_element_by_id('txtPword')
        self.login = self.driver.find_element_by_id('login')

    def fill_username(self, user_name):
        self.username.send_keys(user_name)

    def fill_password(self, password):
        self.password.send_keys(password)

    def click_login(self):
        self.login.click()
