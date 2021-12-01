from unittest import TestCase

from problems.smallest_range import Solution


class TestSolution(TestCase):
    def test_smallest_range_1(self):
        self.assertEqual(Solution().smallestRangeI([7, 8, 8], 5), 1)

    def test_smallest_range_2(self):
        self.assertEqual(Solution().smallestRangeI([0, 10], 2), 6)

    def test_smallest_range_3(self):
        self.assertEqual(Solution().smallestRangeI([1, 3, 6], 3), 3)

    def test_smallest_range_4(self):
        self.assertEqual(Solution().smallestRangeI([9, 9, 2, 8, 7], 4), 3)
