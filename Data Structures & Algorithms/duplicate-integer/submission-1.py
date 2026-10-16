class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = set()
        for i in nums:
            if i in dictionary:
                return True
            dictionary.add(i)
        return False