import unittest
from invoice_calculator import divide_pay


class invoiceCalculatorTests(unittest.TestCase):
    def testDividedPositive(self):
        pay = divide_pay(360,{"Alice":3.0, "Bob": 3.0, "Carol": 6.0})
        self.assertEqual(pay,{"Alice":90.0, "Bob": 90.0, "Carol": 180.0})
       
#     def testDividedNegative(self): ## This test should always come back as a failure.
#         pay = divide_pay(360, {"Alice":3.0, "Bob": 6.0, "Carol": 6})
#         self.assertEqual(pay, {"Alice": 120.0, "Bob": 240.0, "Carol": 20})
            
    def testZeroHourPerson(self):  # way simpler to just call the function and then assertEqual to the answers.
        pay = divide_pay(360.0, {"Alice": 3.0, "Bob": 6.0, "Carol": 0.0})
        self.assertEqual(pay, {"Alice": 120.0, "Bob": 240.0, "Carol": 0.0}) 
        
    def testZeroHoursTotal(self):
        with self.assertRaises(ValueError):
            pay = divide_pay(360.0, {"Alice": 0.0, "Bob": 0.0, "Carol": 0.0})
        
    def testNoPeople(self):
        with self.assertRaises(ValueError):
            pay = divide_pay(360.0, {}) 
            
    def testNegativeHours(self):
        with self.assertRaises(ValueError):
            pay = divide_pay(360.0, {"Alice": 3, "Bob": 6, "Carol": -6.0}) 
    

if __name__ == "__main__":
    unittest.main()
    
# assertEqual(first, second, msg=None)
# Test that first and second are equal. If the values do not compare equal, the test will fail.

# In addition, if first and second are the exact same type and one of list, tuple, dict, set, frozenset or str or any type that a subclass registers with addTypeEqualityFunc() the type-specific equality function will be called in order to generate a more useful default error message (see also the list of type-specific methods).

# Changed in version 3.1: Added the automatic calling of type-specific equality function.

# Changed in version 3.2: assertMultiLineEqual() added as the default type equality function for comparing strings.