# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            
            return 1 + max(depth(node.left), depth(node.right))
        
        if not root:
            return 0
        
        left = depth(root.left)
        right = depth(root.right)

        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), left+right, depth(root)-1)