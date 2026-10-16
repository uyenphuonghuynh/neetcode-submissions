class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in preMap:
                return [preMap[complement], i]
            preMap[n] = i
        return -1