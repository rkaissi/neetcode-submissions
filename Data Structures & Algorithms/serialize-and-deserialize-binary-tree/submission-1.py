# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = ["N"] * 1000

        def dfs(node, arr, i):
            if not node:
                return
            arr[i] = str(node.val)
            dfs(node.left, arr, 2*i + 1)
            dfs(node.right, arr, 2*i + 2)
        
        dfs(root, arr, 0)
        return ",".join(arr)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")

        def dfs(arr, i):
            if i >= len(arr) or arr[i] == "N":
                return None
            root = TreeNode(int(arr[i]))
            root.left = dfs(arr, 2*i + 1)
            root.right = dfs(arr, 2*i + 2)
            return root
        
        return dfs(arr, 0)