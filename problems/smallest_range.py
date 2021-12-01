import math
from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        size_A = len(A)
        sum_A = sum(A)
        avg_A = sum_A / size_A

        B = []
        first = A.pop(0)
        if first > avg_A:
            B.append(first - K)
        else:
            B.append(first + K)

        min_B = B[0]
        max_B = B[0]
        diff = 0

        for i in A:
            for option in [i+K, i-K]:
                abs_diff =

        return max(B) - min(B)

