# Definition for singly-linked list with a arb pointer.
# class arbListNode:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.arb = None

class Solution:
    # @param head, a arbListNode
    # @return a arbListNode
    def copyList(self, head):
        dis  = {}
        curr = head
        while curr != None:
            dis[curr] = Node(curr.data)
            curr = curr.next
        curr = head
        while curr != None:
            if curr.next != None:
                dis[curr].next = dis[curr.next]
            else:
                dis[curr].next = None
            if curr.arb:
                dis[curr].arb = dis[curr.arb]
            else:
                dis[curr].arb = None
            curr = curr.next
        return dis[head]
