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
        self.arr = []
        def preorder(root):
            if not root:
                return 
            self.arr.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return self.arr
