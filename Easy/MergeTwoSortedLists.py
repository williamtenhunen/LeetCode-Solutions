from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2
        
        return dummy.next

def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged = Solution().mergeTwoLists(list1, list2)
print(linked_list_to_list(merged))

list1 = create_linked_list([])
list2 = create_linked_list([])
merged = Solution().mergeTwoLists(list1, list2)
print(linked_list_to_list(merged)) 

list1 = create_linked_list([])
list2 = create_linked_list([0])
merged = Solution().mergeTwoLists(list1, list2)
print(linked_list_to_list(merged))