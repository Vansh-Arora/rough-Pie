# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        #  List is empty or has only 1 element
        if not A or not A.next:
            return A
        # More than 1 element
        node = A
        while node != None and node.next != None:
            key = node.next
            prev = node
            # 3 cases sof linked list
            # C1: INSERT AT END
            # C2: INSERT IN BEGINNING
            # C3: INSERT IN BETWEEN

            # C1
            if key.val >= prev.val:
                node = key
            # C2
            elif key.val < A.val:
                prev.next = key.next # Remove key from its position
                key.next = A
                A = key
                node = key

            # C3
            else:
                temp = A
                while key.val > temp.next.val:
                    temp = temp.next 
                prev.next = key.next # Remove key from its position
                key.next = temp.next
                temp.next = key
                node = key
        return A