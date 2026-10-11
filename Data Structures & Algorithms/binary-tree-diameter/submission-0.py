# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res =0
        def traverse_dfs(root):
            nonlocal res
            if not root:
                return 0
            left = traverse_dfs(root.left
            )
            right = traverse_dfs(root.right)
            res = max(res,left+right)
            return 1+max(left,right)
        traverse_dfs(root)
        return res