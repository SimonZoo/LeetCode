# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.arr = []
        def postorder(root):
            if not root:
                return 
            postorder(root.left)
            postorder(root.right)
            self.arr.append(root.val)
            
        postorder(root)
        return self.arr
