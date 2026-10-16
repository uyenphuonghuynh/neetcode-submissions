class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) <=1:
            return nums[0]
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]: # go right
                l = m + 1
            else: # go left
                r = m 
            
        
        return nums[l]


