from selenium impoprt webdriver


class BranchDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome(executable_path="")
        self.newbranchButton = self.driver.find_element_by_id("BtnNewBR")

    def click_new_branches_button(self):
        self.newbranchButton.click()