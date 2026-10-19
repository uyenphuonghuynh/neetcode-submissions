# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return
        while root:
            #gotta find q and p first:
            lca = root
            if root.val < p.val and root.val < q.val:
                #go right
                root = root.right
            elif root.val > p.val and root.val > q.val:
                #go left:
                root = root.left

            else: break
        return root