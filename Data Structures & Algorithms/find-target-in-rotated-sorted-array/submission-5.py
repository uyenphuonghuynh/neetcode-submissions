class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        #finding the rotating point
        while l < r:
            m = l + (r-l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 
        #left here is the rotating point not m 

        #checking which segment target is in:
        def binary_search(l, r):
            while l <= r:
                m = l+ (r-l)//2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        if target >= nums[l] and target <= nums[-1]: #right segment:
            return binary_search(l, len(nums) - 1)
        return binary_search(0, l - 1)

        

