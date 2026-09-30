# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        inorderMap = {}

        for i, val in enumerate(inorder):
            inorderMap[val] = i

        self.i = 0

        def dfs(l, r):
            if l > r:
                return None

            rootVal = preorder[self.i]
            pivot = inorderMap[rootVal]
            self.i += 1
            left = dfs(l, pivot-1)
            right = dfs(pivot+1, r)

            return TreeNode(rootVal, left, right)
        
        return dfs(0, len(inorder)-1)
