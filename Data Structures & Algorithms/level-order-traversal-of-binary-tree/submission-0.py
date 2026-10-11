# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        res=[]
        if root:
            q.append(root)
        while len(q)>0: 
            val =[]
            for i in range(len(q)):
                cur=q.pop(0)
                val.append(cur.val)

                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            res.append(val)
        return res