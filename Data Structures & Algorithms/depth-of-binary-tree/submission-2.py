# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root,1]]
        res = 0
        while stack:
            node, depth =  stack.pop()

            if node:
                res = max(res,depth)
                stack.append([node.left,depth+1]) 
                stack.append([node.right,depth+1]) 
        return res

        # if root is None:
        #     return 0
        # def depth(node):
        #     count_left = 1
        #     count_right = 1
        #     cur =node
        #     if cur.left:
        #         count_left +=1
        #         depth(cur)
        #     if cur.right:
        #         count_right += 1
        #         depth(cur)
        # depth(root)
        # return max(count_left,count_right)
        
        # depth_left = 1
        # depth_right = 1
        # cur = root
        # if cur.left is not None:
        #     depth_left +=1
        #     cur =cur.left
        # if cur.right is not None:
        #     depth_right +=1
        #     cur =cur.right
        # return max(depth_left,depth_right)
