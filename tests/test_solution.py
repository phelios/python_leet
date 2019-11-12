from unittest import TestCase
from problems.num_islands import NumIslands


class TestNumIslands(TestCase):
    def test_get_gap_adj(self):
        data = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
        actual = NumIslands().numIslands(data)
        self.assertEqual(1, actual)

        # data = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
        # actual = NumIslands().numIslands(data)
        # self.assertEqual(1, actual)
