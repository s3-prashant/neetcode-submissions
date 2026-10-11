# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         cur = head
#         nodes = []
#         while cur:
#             nodes.append(cur)
#             cur = cur.next
#         if n == 1:
#             return head.next
        
#         cur = head
#         for i in range(len(nodes)-1):
#             if i+1==n :
#                 # if nodes[i] is not None:
#                     print(i)
#                     print(nodes[i].val)   
#                     # nodes[i].next= nodes[i].next.next
#                     cur.next = cur.next.next
#                     break
#             cur =cur.next

#         return head










#         # cur = head
#         # prev = head

#         # for i in range(n):
#         #     prev = cur
#         #     cur = cur.next
#         # # cur=cur.next
#         # print("prev",prev.val)
#         # prev.next = cur.next
#         # print(cur.val)
#         # cur.next = None

#         # # cur=cur.next.next
#         # # head=cur
#         # return prev
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next
        
        removeIndex = N - n
        if removeIndex == 0:
            return head.next
        
        cur = head
        for i in range(N - 1):
            if (i + 1) == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head