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
        node = head
        while node is not None:
            counter_nodes += 1
            node = node.next
        pos_pop = counter_nodes - n + 1

        # pop
        # first
        if pos_pop == 1:
            return head.next
        # last
        elif pos_pop == counter_nodes: # or n == 1 
            node = head
            init_node = node
            for i in range(1, pos_pop - 1):
                node = node.next
            node.next = None
        # middle
        else:
            # [1,2,3,4,5] n = 3 
            node = head
            init_node = node
            for i in range(1, pos_pop - 1):
                node = node.next
            # connection
            next_node = node.next.next
            node.next = next_node
            # finish list
        return init_node
