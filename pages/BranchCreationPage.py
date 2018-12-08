from selenium import webdriver
from selenium.webdriver.support.select import Select

class BranchCreationPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome(executable_path="")
        self.branchname = self.driver.find_element_by_xpath("//input[@id='txtbName']")
        self.address1 = self.driver.find_element_by_xpath("//input[@id='txtAdd1']")
        self.zipcode = self.driver.find_element_by_xpath("//input[@id='txtZip']")
        self.area = self.driver.find_element_by_xpath("//input[@id='txtArea']")
        self.country = self.driver.find_element_by_xpath("//select[@id='lst_counrtyU']")
        self.city = self.driver..find_element_by_xpath("//select[@id='lst_cityI']")
        self.state = self.driver.find_element_by_xpath("//select[@id='lst_stateI']")
        self.submitbutton = self.driver.find_element_by_xpath("//input[@id='btn_insert']")

    def fill_branchname(self, branch_name):
        self.branchname.sendKeys(branch_name)

    def fill_address1(self, address1):
        self.address1.sendKeys(address1)

    def fill_zipcode(self, zip_code):
        self.zipcode.sendKeys(zip_code)

    def fill_area(self, area):
        self.area.sendKeys(area)

    def select_country(self, country):
        select(self,country).select_by_visible_text("INDIA")

    def  select_city(self, city):
         select(self,city).select_by_visible_text("Hderabad")

    def  select_state(self, state):
         select(self,state).select_by_visible_text("Andhra Pradesh")

    def click_submit_button(self):
        self.submitButton.click()