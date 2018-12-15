import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

from pages.AdminHomePage import AdminHomePage
from pages.BankHomePage import BankHomePage
from pages.BranchCreationPage import BranchCreationPage
from pages.BranchDetailsPage import BranchDetailsPage

import tests.excel_helper as excel

class BranchCreationTest(unittest.TestCase):

    def login(self):
        self.bank_home_page.fill_username("Admin")
        self.bank_home_page.fill_password("Admin")
        self.bank_home_page.click_login()

    # test fixture
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='E:\selenium\softwares\drivers\chromedriver.exe')
        self.driver.get("http://srssprojects.in")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.bank_home_page = BankHomePage(self.driver)
        self.admin_home_page = AdminHomePage(self.driver)
        self.branch_details_page = BranchDetailsPage(self.driver)
        self.branch_creation_page = BranchCreationPage(self.driver)

        sleep(2)
        self.login()
        sleep(2)

    # login test
    def test_01_login(self):
        self.assertTrue(self.admin_home_page.logoutButton.is_displayed(), "login test passed")

    def test_02_branch_creation(self):
        self.admin_home_page.click_branches_button()
        self.branch_details_page.click_new_branches_button()
        self.branch_creation_page.fill_branch_creation_from("andamanbranchOn", "usmansagar", "54345")
        self.branch_creation_page.click_submit_button()
        alerttext = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.assertTrue("New Branch with id" in alerttext, alerttext)

    def test_03_branch_creation_reset(self):
        self.admin_home_page.click_branches_button()
        self.branch_details_page.click_new_branches_button()
        option = self.branch_creation_page.get_country_default_option()
        self.branch_creation_page.fill_branch_creation_from("andamanbranch", "usmansagar", "54345")
        self.branch_creation_page.click_reset_button()
        self.assertTrue("Select" == option)

    def test_04_branch_creation_cancel(self):
        self.admin_home_page.click_branches_button()
        self.branch_details_page.click_new_branches_button()
        self.branch_creation_page.click_cancel_button()
        self.assertTrue(self.branch_details_page.newbranchButton.is_displayed())

    def test_05_branch_creation_data_driven(self):
        excel.open_workbook('E:\SMIT\sneha\sneha_bank\TestData.xlsx','BranchData')
        nor = excel.get_row_count()
        for row in range(2, nor):
            branch_name = excel.read_cell_data(row, 1)
            address1 = excel.read_cell_data(row, 2)
            zipcode = excel.read_cell_data(row, 3)
            country = excel.read_cell_data(row, 4)
            state = excel.read_cell_data(row, 5)
            city = excel.read_cell_data(row, 6)
            self.admin_home_page.click_branches_button()
            self.branch_details_page.click_new_branches_button()
            self.branch_creation_page.fill_branch_creation_from(branch_name, address1, zipcode, country, state, city)
            self.branch_creation_page.click_submit_button()
            alerttext = self.driver.switch_to.alert.text
            self.driver.switch_to.alert.accept()
            self.assertTrue("New Branch with id" in alerttext, alerttext)

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
