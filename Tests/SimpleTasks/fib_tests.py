import unittest
from SimpleTasks.fib import *


class FibTestCase(unittest.TestCase):
    def test_fib1(self):
        with self.assertRaises(RecursionError):
            fib1(5)

    def test_fib2(self):
        self.assertEqual(fib2(6), 8)

    def test_fib3(self):
        self.assertEqual(fib3(6), 8)

    def test_fib4(self):
        self.assertEqual(fib4(6), 8)

    def test_fib5(self):
        self.assertEqual(fib5(6), 8)

    def test_fib6(self):
        result = fib6(5)
        self.assertEqual([0, 1, 1, 2, 3, 5], list(result))


if __name__ == '__main__':
    unittest.main()
