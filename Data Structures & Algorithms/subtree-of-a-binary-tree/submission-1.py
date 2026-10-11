# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False
        def subtree(p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return subtree(p.left,q.left) and subtree(p.right,q.right)
            else:
                return False

        if subtree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        # if cur.val == subRoot.val:
        #     subtree(cur,SubRoot)
        # elif cur.left.val == subRoot.val:
        #     subtree(cur.left,subRoot)
        # else:
        #     subtree(cur.right,subRoot)
            