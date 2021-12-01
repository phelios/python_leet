from unittest import TestCase
from problems.robber import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.s = Solution()

    def test_rob(self):
        self.assertEqual(self.s.rob([2, 7, 9, 3, 1]), 12)

    def test_rob_empty(self):
        self.assertEqual(self.s.rob([]), 0)

    def test_rob_2_elem(self):
        self.assertEqual(self.s.rob([1, 2]), 2)

    def test_rob_3_elem(self):
        self.assertEqual(self.s.rob([12, 21, 2]), 21)

    def test_rob_last_100(self):
        self.assertEqual(self.s.rob([1, 3, 1, 3, 100]), 103)

    def test_rob_last_106(self):
        self.assertEqual(self.s.rob([1, 3, 1, 100, 1, 3, 100]), 203)

    def test_rob_last_16(self):
        self.assertEqual(self.s.rob([2, 4, 8, 9, 9, 3]), 19)

    def test_rob_last_39(self):
        self.assertEqual(self.s.rob([6, 3, 10, 8, 2, 10, 3, 5, 10, 5, 3]), 39)

    def test_edges(self):
        self.assertEqual(self.s.rob([3, 2, 4, 5]), 8)
