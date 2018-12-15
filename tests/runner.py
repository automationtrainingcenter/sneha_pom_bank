import unittest
import os

from HtmlTestRunner import HTMLTestRunner

from tests.BranchTest import BranchCreationTest

# suite creation
branch_creation_tests = unittest.TestLoader().loadTestsFromTestCase(BranchCreationTest)
bc_suite = unittest.TestSuite([branch_creation_tests])

dir = os.getcwd()

# test runner
# unittest.TextTestRunner().run(bc_suite)
suite_runner = HTMLTestRunner(output=dir,
                        report_title='Branch creation report',
                        descriptions='branch creation with valid data')

suite_runner.run(bc_suite)
