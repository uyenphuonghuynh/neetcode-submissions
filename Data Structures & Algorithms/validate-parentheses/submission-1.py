class Solution:
    def isValid(self, s: str) -> bool:
        closeddict = {"{":"}", "[":"]", "(":")"}
        stack = []
        for c in s:
            if c in closeddict:
                stack.append(closeddict[c])
            else:
                if not stack:
                    return False
                val = stack.pop()
                if c != val:
                    return False
        return True if not stack else False
