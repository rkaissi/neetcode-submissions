# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = [root, left, right, ...]
        inMap = {}

        for i, n in enumerate(inorder):
            inMap[n] = i

        self.preIdx = 0
        def construct(l, r):
            if l > r:
                return None
            
            val = preorder[self.preIdx]
            self.preIdx += 1
            node = TreeNode(val)
            inIdx = inMap[val]

            node.left = construct(l, inIdx-1)
            node.right = construct(inIdx+1, r)
            return node

        return construct(0, len(preorder)-1)

