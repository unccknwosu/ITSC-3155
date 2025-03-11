import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(3, 2), 5)
        self.assertEqual(Calculator().add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(Calculator().subtract(10, 5), 5)
        self.assertEqual(Calculator().subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(Calculator().multiply(3, 4), 12)
        self.assertEqual(Calculator().multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(Calculator().divide(10, 2), 5)
        self.assertEqual(Calculator().divide(9, 3), 3)
    
if __name__ == "__main__":
    unittest.main()