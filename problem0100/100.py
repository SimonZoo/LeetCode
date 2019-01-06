# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
    
        if p == None or q == None:
            return p == q
        return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
