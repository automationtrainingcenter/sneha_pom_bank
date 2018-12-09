from selenium.webdriver.support.select import Select


class BranchCreationPage:

    def __init__(self, driver):
        self.driver = driver
        self.branchname = self.driver.find_element_by_xpath("//input[@id='txtbName']")
        self.address1 = self.driver.find_element_by_xpath("//input[@id='txtAdd1']")
        self.zipcode = self.driver.find_element_by_xpath("//input[@id='txtZip']")
        self.area = self.driver.find_element_by_xpath("//input[@id='txtArea']")
        self.country = self.driver.find_element_by_xpath("//select[@id='lst_counrtyU']")
        self.city = self.driver.find_element_by_xpath("//select[@id='lst_cityI']")
        self.state = self.driver.find_element_by_xpath("//select[@id='lst_stateI']")
        self.submitbutton = self.driver.find_element_by_xpath("//input[@id='btn_insert']")
        self.reset_button = "Btn_Reset"
        self.cancel_button = "Btn_cancel"

    def fill_branchname(self, branch_name):
        self.branchname.send_keys(branch_name)

    def fill_address1(self, address1):
        self.address1.send_keys(address1)

    def fill_zipcode(self, zip_code):
        self.zipcode.send_keys(zip_code)

    def fill_area(self, area):
        self.area.send_keys(area)

    def select_country(self, country):
        Select(self.country).select_by_visible_text(country)

    def select_city(self, city):
        self.city = self.driver.find_element_by_xpath("//select[@id='lst_cityI']")
        Select(self.city).select_by_visible_text(city)

    def select_state(self, state):
        self.state = self.driver.find_element_by_xpath("//select[@id='lst_stateI']")
        Select(self.state).select_by_visible_text(state)

    def click_submit_button(self):
        self.submitbutton = self.driver.find_element_by_xpath("//input[@id='btn_insert']")
        self.submitbutton.click()

    def click_reset_button(self):
        self.driver.find_element_by_id(self.reset_button).click()

    def click_cancel_button(self):
        self.driver.find_element_by_id(self.cancel_button).click()

    def fill_branch_creation_from(self, branch_name, address1, zipcode, country="INDIA", state="Andhra Pradesh",
                                  city="Hyderabad"):
        self.fill_branchname(branch_name)
        self.fill_address1(address1)
        self.fill_zipcode(zipcode)
        self.select_country(country)
        self.select_state(state)
        self.select_city(city)
