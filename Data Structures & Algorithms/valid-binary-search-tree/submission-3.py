# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = [(root, float('-inf'), float('inf'))]
        rightVal = root.val
        while queue:
            qLen = len(queue)
            for i in range(qLen):
                curr, lower, upper = queue.pop(0)
                if not lower < curr.val < upper:
                    return False
                if curr.left:
                    if curr.left.val < curr.val:
                        queue.append((curr.left, lower, curr.val))
                    else:
                        return False
                if curr.right:
                    if curr.right.val > curr.val:
                        queue.append((curr.right, curr.val, upper))
                    else:
                        return False
        return True
