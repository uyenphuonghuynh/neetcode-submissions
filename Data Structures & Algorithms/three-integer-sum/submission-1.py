class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r = 0, len(nums) - 1
        nums.sort()
        res = []
        if not nums:
            return []
        def binary_search(bl, br, x):
            while bl <= br:
                m = (br + bl) // 2
                if nums[m] == x:
                    return True
                elif nums[m] < x:
                    bl = m + 1
                else:
                    br = m - 1
            return False
        while l < len(nums) - 2:
            temp = [nums[l], nums[r]]
            x = - (nums[r] + nums[l])
            if binary_search(l+1, r-1, x):
                temp.append(x)
                if temp not in res:
                    res.append(temp)
            if l == (r):
                l += 1
                r = len(nums)
            r -= 1
        return res