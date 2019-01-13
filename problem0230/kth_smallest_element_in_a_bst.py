# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def count(cur):
            if not cur:
                return 0
            return 1+count(cur.left)+count(cur.right)
        
        while root:
            cnt = count(root.left)
            if cnt > k-1:
                root = root.left
            elif cnt < k-1:
                k -= cnt + 1
                root = root.right
            else:
                return root.val
