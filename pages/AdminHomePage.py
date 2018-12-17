class AdminHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.branchesButton = "//a[@href='admin_banker_master.aspx']"
        self.rolesButton = "//a[@href='Admin_Roles_details.aspx']"
        self.employeeButton = "//a[@href='Admin_Emp_details.aspx']"
        self.logoutButton = "//a[@href='home.aspx']"
        self.homeButton = "//a[@href='adminflow.aspx']"

    def click_branches_button(self):
        self.driver.find_element_by_xpath(self.branchesButton).click()

    def click_roles_button(self):
        self.driver.find_element_by_xpath(self.rolesButton ).click()

    def click_employee_button(self):
        self.driver.find_element_by_xpath(self.employeeButton).click()

    def click_logout_button(self):
        self.driver.find_element_by_xpath(self.logoutButton).click()

    def click_home_button(self):
        self.driver.find_element_by_xpath(self.homeButton).click()

    def is_Logout_displayed(self):
       return self.driver.find_element_by_xpath(self.logoutButton).is_displayed()
