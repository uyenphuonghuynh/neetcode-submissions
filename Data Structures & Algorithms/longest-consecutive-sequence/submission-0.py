class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        #only count if its the begining of the set: 
        for i in nums:
            if i - 1 in nums:
                continue
            length = 1
            while i + length in nums:
                length += 1
            res = max(res, length)
        return res
            