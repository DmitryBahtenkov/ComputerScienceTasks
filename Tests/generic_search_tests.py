import unittest
from SearchTasks.generic_search import *


class GenericSearchTestCase(unittest.TestCase):
    def test_contains(self):
        l = [1,2,3,4,5,6,7,8,9,10]
        self.assertTrue(linear_contains(l, 7))

    def test_not_contains(self):
        l = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(linear_contains(l, 11), False)

    def test_binary_contains(self):
        l = [1,2,3,4,5,6,7,8,9,10]
        self.assertTrue(binary_contains(l, 7))

    def test_binary_not_contains(self):
        l = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(binary_contains(l, 11), False)

if __name__ == '__main__':
    unittest.main()
