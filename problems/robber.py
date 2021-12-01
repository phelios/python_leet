from typing import List


class Solution:
    def rob(self, nums: List[int], total=0) -> int:

        if len(nums) < 4:
            nums = nums + ([0] * (4 - len(nums)))

        nums[1] = max(nums[0], nums[1])

        for k in range(2, len(nums)):
            new_tot = nums[k] + nums[k-2]
            if new_tot > nums[k-1]:
                nums[k] = new_tot
            else:
                nums[k] = nums[k-1]

        return nums[-1]



