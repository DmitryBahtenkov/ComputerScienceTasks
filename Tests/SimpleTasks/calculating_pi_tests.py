import unittest
from SimpleTasks.calculationg_pi import *
import math


class CalculatingPiTestCase(unittest.TestCase):
    def test_two_terms(self):
        self.assertEqual(round(calculate_pi(300), 2), 3.14)


if __name__ == '__main__':
    unittest.main()
