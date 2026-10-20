# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        if not root:
            return []
        result = [[root.val]]
        curr = TreeNode()
        while queue:
            #getting the children
            qLen = len(queue)
            stack = []
            for c in range(qLen):
                curr = queue.pop(0)

                if curr.left:
                    stack.append(curr.left.val)
                    queue.append(curr.left)
                if curr.right:
                    stack.append(curr.right.val)
                    queue.append(curr.right)
            if stack:
                result.append(stack) 
        return result












