from unittest import TestCase
from problems.container_with_most_water import Solution


class TestSolution(TestCase):
    def test_get_gap_adj(self):
        actual = Solution().get_gap_adj(5, 1, 1)
        self.assertEqual(1, actual)

    def test_convert(self):
        actual = Solution().convert("PAYPALISHIRING", 5)
        self.assertEqual("PHASIYIRPLIGAN", actual)