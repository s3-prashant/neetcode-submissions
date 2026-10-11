# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        # while fast and fast.next:
            
        #     slow = slow.next
        #     fast = fast.next.next
        #     if fast == slow:
        #         return True
        # return False

        cur = head
        visit = set()
        while cur:
            if cur in visit:
                return True
            visit.add(cur)
            cur = cur.next
        return False


        # fast , slow = head, head

        # while fast is not None and fast.next is not None:
        #     fast = fast.next.next
        #     slow = slow.next

        #     if slow == fast:
        #         return True
        # return False