import unittest
from invoice_calculator import divide_pay


class InvoiceCalculatorTests(unittest.TestCase):
    def testDividedFairly(self):
        self.answers = {"Alice": 90, "Bob": 90, "Carol": 180}
        self.amount = 360.0
        self.staff_hours = {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0}
            
        result_dict = divide_pay(self.amount,self.staff_hours)
        print "result_dict",result_dict
        
        for staff, result in self.answers.iteritems():
            print staff,result,result_dict[staff]
            self.assertEqual(result,result_dict[staff])
#         Alice and Bob work for 3 hours, and Carol works for 6 hours on a $360 project.

if __name__ == "__main__":
    unittest.main()
    
# assertEqual(first, second, msg=None)
# Test that first and second are equal. If the values do not compare equal, the test will fail.

# In addition, if first and second are the exact same type and one of list, tuple, dict, set, frozenset or str or any type that a subclass registers with addTypeEqualityFunc() the type-specific equality function will be called in order to generate a more useful default error message (see also the list of type-specific methods).

# Changed in version 3.1: Added the automatic calling of type-specific equality function.

# Changed in version 3.2: assertMultiLineEqual() added as the default type equality function for comparing strings.