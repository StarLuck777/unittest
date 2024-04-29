import unittest
import test_calc2

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(test_calc2.CalcBasicTest))
calcTestSuite.addTest(unittest.makeSuite(test_calc2.CalcExTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)
