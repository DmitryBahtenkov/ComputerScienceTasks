import unittest
from SimpleTasks.hanoi import *
from DataStructures.stack import *
from typing import Tuple


class HanoiTestCase(unittest.TestCase):
    @staticmethod
    def setup(num: int) -> Tuple[Stack[int], Stack[int], Stack[int]]:
        tower_a: Stack[int] = Stack()
        tower_b: Stack[int] = Stack()
        tower_c: Stack[int] = Stack()
        for i in range(1, num + 1):
            tower_a.push(i)

        return tower_a, tower_b, tower_c,

    def test_three_equal(self):
        tower_a, tower_b, tower_c = self.setup(3)
        hanoi(tower_a, tower_b, tower_c, 3)
        self.assertEqual('[1, 2, 3]', repr(tower_b))


if __name__ == '__main__':
    unittest.main()
