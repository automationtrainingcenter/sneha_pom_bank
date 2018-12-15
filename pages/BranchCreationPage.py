from selenium.webdriver.support.select import Select


class BranchCreationPage:

    def __init__(self, driver):
        self.driver = driver
        self.branchname = "//input[@id='txtbName']"
        self.address1 = "//input[@id='txtAdd1']"
        self.zipcode = "//input[@id='txtZip']"
        self.area = "//input[@id='txtArea']"
        self.country = "//select[@id='lst_counrtyU']"
        self.city = "//select[@id='lst_cityI']"
        self.state = "//select[@id='lst_stateI']"
        self.submitbutton = "//input[@id='btn_insert']"
        self.reset_button = "Btn_Reset"
        self.cancel_button = "Btn_cancel"

    def fill_branchname(self, branch_name):
        self.driver.find_element_by_xpath(self.branchname).send_keys(branch_name)

    def fill_address1(self, address1):
        self.driver.find_element_by_xpath(self.address1).send_keys(address1)

    def fill_zipcode(self, zip_code):
        self.driver.find_element_by_xpath(self.zipcode).send_keys(zip_code)

    def fill_area(self, area):
        self.driver.find_element_by_xpath(self.area).send_keys(area)

    def select_country(self, country):
        Select(self.driver.find_element_by_xpath(self.country)).select_by_visible_text(country)

    def get_country_default_option(self):
       return Select(self.driver.find_element_by_xpath(self.country)).first_selected_option.text


    def select_city(self, city):
        self.city = self.driver.find_element_by_xpath(self.city)
        Select(self.city).select_by_visible_text(city)

    def select_state(self, state):
        self.state = self.driver.find_element_by_xpath(self.state)
        Select(self.state).select_by_visible_text(state)

    def click_submit_button(self):
        self.driver.find_element_by_xpath(self.submitbutton).click();

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
