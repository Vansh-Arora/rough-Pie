# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A.next == None or A == None:
            return A
        
        prev = A
        node = prev.next
        
        while node != None:
            if node.val == prev.val:
                if node.next:
                    prev.next = node.next
                else:
                    prev.next = None
            else:
                prev = prev.next
            if prev:
                node = prev.next
            else:
                node = prev
        return A
            
