# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        left, right = self.isSubtree(root.left, subRoot), self.isSubtree(root.right, subRoot)
        return self.sameTree(root, subRoot) or left or right

    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and
                self.sameTree(p.left, q.left) and
                self.sameTree(p.right, q.right))