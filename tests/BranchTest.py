import unittest

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

from pages.AdminHomePage import AdminHomePage
from pages.BankHomePage import BankHomePage
from pages.BranchCreationPage import BranchCreationPage
from pages.BranchDetailsPage import BranchDetailsPage


class BranchCreationTest(unittest.TestCase):
    def login(self):
        self.bank_home_page = BankHomePage(self.driver)
        self.bank_home_page.fill_username("Admin")
        self.bank_home_page.fill_password("Admin")
        self.bank_home_page.click_login()



    # test fixture
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='E:\selenium\softwares\drivers\chromedriver.exe')
        self.driver.get("http://srssprojects.in")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        sleep(2)
        self.login()
        sleep(2)

    # login test
    def test_01_login(self):
        self.admin_home_page = AdminHomePage(self.driver)
        self.assertTrue(self.admin_home_page.logoutButton.is_displayed(), "login test passed")

    def test_02_branch_creation(self):
        self.admin_home_page = AdminHomePage(self.driver)
        self.admin_home_page.click_branches_button()
        self.branch_details_page = BranchDetailsPage(self.driver)
        self.branch_details_page.click_new_branches_button()
        self.branch_creation_page = BranchCreationPage(self.driver)
        self.branch_creation_page.fill_branch_creation_from("andamanbranchOn", "usmansagar", "54345")
        self.branch_creation_page.click_submit_button()
        alerttext = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertTrue("New Branch with id" in alerttext, alerttext)

    def test_03_branch_creation_reset(self):
        self.admin_home_page = AdminHomePage(self.driver)
        self.admin_home_page.click_branches_button()
        self.branch_details_page = BranchDetailsPage(self.driver)
        self.branch_details_page.click_new_branches_button()
        self.branch_creation_page = BranchCreationPage(self.driver)
        option = Select(self.branch_creation_page.country).first_selected_option.text
        self.branch_creation_page.fill_branch_creation_from("andamanbranch", "usmansagar", "54345")
        self.branch_creation_page.click_reset_button()
        self.assertTrue("Select" == option)

    def test_04_branch_creation_cancel(self):
        self.admin_home_page = AdminHomePage(self.driver)
        self.admin_home_page.click_branches_button()
        self.branch_details_page = BranchDetailsPage(self.driver)
        self.branch_details_page.click_new_branches_button()
        self.branch_creation_page = BranchCreationPage(self.driver)
        self.branch_creation_page.click_cancel_button()
        self.branch_details_page = BranchDetailsPage(self.driver)
        self.assertTrue(self.branch_details_page.newbranchButton.is_displayed())

    # logout test
    def test_05_logout(self):
        self.admin_home_page = AdminHomePage(self.driver)
        self.admin_home_page.click_logout_button()
        self.bank_home_page = BankHomePage(self.driver)
        self.assertTrue(self.bank_home_page.login.is_displayed(), "logout test passed")


# test fixture
    def tearDown(self):
        sleep(2)
        self.driver.close()
