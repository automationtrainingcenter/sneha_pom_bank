from selenium import webdriver
from selenium.webdriver.support.select import Select


class BankHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.username = 'txtuId'
        self.password = 'txtPword'
        self.login = 'login'

    def fill_username(self, user_name):
        self.driver.find_element_by_id(self.username).send_keys(user_name)

    def fill_password(self, password):
        self.driver.find_element_by_id(self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login).click()

    def is_login_displayed(self):
        self.driver.find_element_by_id(self.login).is_displayed()