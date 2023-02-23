import unittest

from main import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_division(self):
        self.assertAlmostEqual(self.calc.divide(6, 3), 2.0)
        self.assertRaises(ValueError, self.calc.divide, 6, 0)


if __name__ == '__main__':
    unittest.main()
