class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        win = set()
        l, r = 0, 0
        if len(s) == 1:
            return 1
        if not s:
            return 0
        while l <= r and r < len(s):
            while s[r] in win:
                win.remove(s[l])
                l += 1
            win.add(s[r])
            res = max(res, len(win))
            r += 1
        return res
            