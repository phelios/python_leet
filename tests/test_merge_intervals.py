from unittest import TestCase
from problems.merge_intervals import MergeIntervals


class TestMergeIntervals(TestCase):
    def test_merge(self):
        input = [[1,4],[0,0]]
        expected = [[1,4],[0,0]]
        self.assertEqual(expected, MergeIntervals().merge(input))
