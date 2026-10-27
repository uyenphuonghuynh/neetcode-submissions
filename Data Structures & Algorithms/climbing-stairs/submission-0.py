from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def climb(s):
            if s > n:
                return 0
            if s == n:
                return 1
            return climb(s+1) + climb(s+2)
        return climb(0)
