# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #recursive DFS approach
        def valid(node,left,right):

            if not node:
                return True #empty tree is BST
            
            if  (node.val > left and node.val < right):
                #recursive call left and right nodes
                #for left node left value remians same right boundary changes
                return (valid(node.left,left,node.val) and 
                    valid(node.right,node.val,right))
            else:
                return False
            

        return valid(root,float("-inf"),float("inf"))