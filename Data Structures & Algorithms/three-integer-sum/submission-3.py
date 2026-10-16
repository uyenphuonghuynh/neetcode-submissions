class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #optimal solution
        nums.sort()
        res = []
        for i in range(len(nums) -2):
            if nums[i] > 0:
                break
            if i >0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                s = (nums[l] + nums[r])
                if s + nums[i] == 0:
                    res.append([nums[l], nums[i], nums[r]])
                    r -= 1
                    l += 1
                    #checking duplicate
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif s + nums[i] > 0:
                    r -= 1
                else:
                    l += 1
        return res 