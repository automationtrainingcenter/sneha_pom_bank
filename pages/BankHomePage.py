from selenium import webdriver
from selenium.webdriver.support.select import Select


class BankHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome(executable_path="")
        self.username = self.driver.find_element_by_id('txtuId')
        self.password = self.driver.find_element_by_id('txtPword')
        self.login = self.driver.find_element_by_id('login')

    def fill_username(self, user_name):
        self.username.sendKeys(user_name)

    def fill_password(self, password):
        self.password.sendKeys(password)

    def click_login(self):
        self.login.click()
