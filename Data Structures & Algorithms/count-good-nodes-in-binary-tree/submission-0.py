# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0

        def dfs(node, curMax):
            if not node:
                return
            
            if curMax <= node.val:
                self.goodNodes += 1
            curMax = max(curMax, node.val)
            dfs(node.left, curMax)
            dfs(node.right, curMax)
        
        dfs(root, -100)
        return self.goodNodes