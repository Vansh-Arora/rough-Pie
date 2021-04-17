# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        if not A or not A.next: return None
        count = 0
        node = A
        while node:
            count += 1
            node = node.next
        if B > count:
            return A.next
        count -= B
        node = A
        i = 0
        while i < count-1:
            node = node.next
            i += 1
        if node.next:
            node.next = node.next.next
        else:
            node = node.next
        return A
            
