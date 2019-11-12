from typing import List


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_interval = []
        for index, item in enumerate(intervals):
            merged_item = item
            while index < len(intervals) - 1 and merged_item[1] >= intervals[index+1][0]:

                if merged_item[1] < intervals[index+1][1]:
                    merged_item[1] = intervals[index+1][1]

                if merged_item[0] > intervals[index+1][0]:
                    merged_item[0] = intervals[index+1][0]

                del intervals[index+1]

            merged_interval.append(merged_item)

        return merged_interval
