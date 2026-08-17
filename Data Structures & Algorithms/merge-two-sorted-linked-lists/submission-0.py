# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        returnList = ListNode()
        copy = returnList
        
        while list1 and list2:
            if list1.val <= list2.val:
                copy.next = list1
                list1 = list1.next
            else: # list2 is lower
                copy.next = list2
                list2 = list2.next
            copy = copy.next

        # una de las filas se termina
        copy.next = list1 if list1 else list2

        return returnList.next
        