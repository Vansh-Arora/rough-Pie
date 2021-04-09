# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        p_node = None
        while A != None:
            f_node = A.next
            A.next = p_node
            p_node = A
            A = f_node
        return p_node
