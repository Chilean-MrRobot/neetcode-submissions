# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        elif head.next is None:
            return False

        slow = head.next
        fast = head.next.next
        while slow and fast:
            if slow == fast:
                return True
            else:
                slow = slow.next
                if fast.next:
                    fast = fast.next.next
                else:
                    return False

        return False