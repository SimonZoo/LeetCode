# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out = []
        stack = []
        while root or stack:
            if root:
                out.append(root.val)
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        return out
