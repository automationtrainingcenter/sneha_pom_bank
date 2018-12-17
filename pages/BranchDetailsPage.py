class BranchDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self.newbranchButton = "BtnNewBR"

    def click_new_branches_button(self):
        self.driver.find_element_by_id(self.newbranchButton).click()

    def is_new_branch_displayed(self):
       return self.driver.find_element_by_id(self.newbranchButton).is_displayed()