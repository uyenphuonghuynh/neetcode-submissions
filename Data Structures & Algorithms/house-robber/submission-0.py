from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rob1(n):
            if n >= len(nums):
                return 0
            return max(rob1(n+1), rob1(n+2) + nums[n])
        return rob1(0)