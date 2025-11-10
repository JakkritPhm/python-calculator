import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)
    
    def test_sub2(self):
        self.assertEqual(self.calc.subtract(12, 5), -7)

    def test_mult(self):
        self.assertEqual(self.calc.multiply(12, 5), 60)

    def test_mult2(self):
        self.assertEqual(self.calc.multiply(9, 6), 54)

    def test_div(self):
        self.assertEqual(self.calc.divide(3, 1), 3)
    
    def test_div2(self):
        self.assertEqual(self.calc.divide(25, 5), 5)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(40, 5), 0)

    def test_mod2(self):
        self.assertEqual(self.calc.modulo(15 ,2), 1)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()