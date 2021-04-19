# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if not A or not A.next:
            return A
        node = A
        prev = A
        while node and node.next:
            if prev == A:
                A = node.next
            temp = node.next.next
            prev.next = node.next
            node.next.next = node
            node.next = temp
            prev = node
            node = node.next
        return A