import unittest

from HtmlTestRunner import HTMLTestRunner

from tests.BranchTest import BranchCreationTest

# suite creation
branch_creation_tests = unittest.TestLoader().loadTestsFromTestCase(BranchCreationTest)
bc_suite = unittest.TestSuite([branch_creation_tests])



# test runner
# unittest.TextTestRunner().run(bc_suite)
runner = HTMLTestRunner(output="E:\\SMIT\\sneha\\sneha_bank\\reports",
                        report_title='Branch creation report',
                        descriptions='branch creation with valid data')

runner.run(bc_suite)
