from unittest import TestCase
from problems.container_with_most_water import Solution


class TestSolution(TestCase):
    def test_maxArea(self):
        test_input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        self.assertEqual(expected, Solution().maxArea(test_input))
