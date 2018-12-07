class AdminHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.branchesButton = self.driver.find_element_by_xpath("//a[@href='admin_banker_master.aspx']")
        self.rolesButton = self.driver.find_element_by_xpath("//a[@href='Admin_Roles_details.aspx']")
        self.employeeButton = self.driver.find_element_by_xpath("//a[@href='Admin_Emp_details.aspx']")
        self.logoutButton = self.driver.find_element_by_xpath("//a[@href='home.aspx']")
        self.homeButton = self.driver.find_element_by_xpath("//a[@href='adminflow.aspx']")

    def click_branches_button(self):
        self.branchesButton.click()

    def click_roles_button(self):
        self.rolesButton.click()

    def click_employee_button(self):
        self.employeeButton.click()

    def click_logout_button(self):
        self.logoutButton.click()

    def click_home_button(self):
        self.homeButton.click()
