import unittest
import UnitTests

testCases = []
testCases.append(UnitTests.Program_tests)

testLoad = unittest.TestLoader()

suites = []
suites.append(testLoad.loadTestsFromTestCase(testCases[0]))

res_suite = unittest.TestSuite(suites)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(res_suite)