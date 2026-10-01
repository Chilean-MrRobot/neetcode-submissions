# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_node = ListNode() 
        dummy = sum_node 
        next_one = 0
        while (l1 is not None) or (l2 is not None):         
            sum_val = next_one
            if l1 is not None:
                sum_val += l1.val
            if l2 is not None:
                sum_val += l2.val

            if sum_val >= 10:
                sum_val -= 10
                next_one = 1
            else:
                next_one = 0

            sum_node.next = ListNode(val=sum_val)
            sum_node = sum_node.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if next_one == 1:
            sum_node.next = ListNode(val=next_one)

        return dummy.next

            

