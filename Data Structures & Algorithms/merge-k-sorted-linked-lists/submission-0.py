# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = []

        for node in lists:
            cur=node
            while cur:
                res.append(cur.val)
                cur= cur.next
        
        # print(sorted(res))
        res.sort()

        temp = head = ListNode()
        i=0
        while i < len(res):
            temp.next = ListNode(res[i])
            i += 1
            temp =temp.next
        return head.next


        