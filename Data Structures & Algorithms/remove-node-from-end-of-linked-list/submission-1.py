# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if one node list
        if head.next is None:
            return None

        # Check length
        counter_nodes = 0
        dummy = ListNode(next=head)
        node = dummy
        while node.next is not None:
            counter_nodes += 1
            node = node.next
        pos_pop = counter_nodes - n + 1

        # pop
        node = dummy
        for i in range(1, pos_pop):
            node = node.next
        node.next = node.next.next
        return dummy.next