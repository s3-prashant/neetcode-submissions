# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         
        #  head1 = list1
        #  head2 = list2

        dummy = newnode = ListNode()

        while list1 and list2:

            if list1.val < list2.val:
                newnode.next = list1
                list1 = list1.next
            else:
                newnode.next = list2
                list2 = list2.next
            newnode =newnode.next
        
        if list1:
            newnode.next = list1
            list1 = list1.next
            newnode =newnode.next
        if list2:
            newnode.next = list2
            list2 = list2.next
            newnode =newnode.next
        
        return dummy.next




        #  dummy = new_node = ListNode()
        #  while list1 and list2:
             
        #     if list1.val < list2.val:
        #         new_node.next = list1
        #         list1 = list1.next
        #     else:
        #         new_node.next = list2
        #         list2 = list2.next
        #     new_node = new_node.next
        
        #     print(new_node)
        #  new_node.next = list1 or list2
        #  print  (new_node.next.val)
        #  return dummy.next
