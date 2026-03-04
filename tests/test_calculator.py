"""
Unit tests for Calculator class
Demonstrates comprehensive testing for Jenkins CI/CD
"""

import unittest
import sys
import os

# Add parent directory to path to import calculator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers"""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers"""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
    
    def test_subtract(self):
        """Test subtraction"""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
    
    def test_multiply(self):
        """Test multiplication"""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division"""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333333, places=5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_power(self):
        """Test power operation"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
    
    def test_modulo(self):
        """Test modulo operation"""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(15, 4), 3)
    
    def test_modulo_by_zero(self):
        """Test modulo by zero raises error"""
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)
    
    # Uncomment this test to demonstrate a FAILING build in Jenkins
    # def test_intentional_failure(self):
    #     """This test is intentionally wrong to show Jenkins failure detection"""
    #     self.assertEqual(self.calc.add(2, 2), 5)  # Wrong answer!


class TestCalculatorEdgeCases(unittest.TestCase):
    """Test edge cases"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.calc = Calculator()
    
    def test_large_numbers(self):
        """Test with very large numbers"""
        self.assertEqual(self.calc.add(999999999, 1), 1000000000)
    
    def test_floating_point(self):
        """Test with floating point numbers"""
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=10)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=10)


def suite():
    """Create test suite"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCalculator))
    test_suite.addTest(unittest.makeSuite(TestCalculatorEdgeCases))
    return test_suite


if __name__ == '__main__':
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
