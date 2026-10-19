# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.righttps://neetcode.io/user/SharpCarnage461$0ht = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root, subroot):
            #case1 both are none
            if not root and not subroot:
                return True
            
            #case2 only 1 is None 
            if not subroot:
                return False
            if not root:
                return False
            
            #case3 different val
            if subroot.val != root.val:
                return False
            
            #recursively check
            return sameTree(root.left, subroot.left) and sameTree(root.right, subroot.right)

        if not root:
            return False
        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
