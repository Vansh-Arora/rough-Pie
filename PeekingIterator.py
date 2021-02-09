# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        self.current = -1
             

        
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasNext:
            print(self.current)
            print(self.List[self.current + 1])
            return self.List[self.current + 1]
        

    def next(self):
        """
        :rtype: int
        """
        print(self.List)
        if self.hasNext:
            print(self.current)
            self.current += 1
            print(self.List[self.current])
            return self.List[self.current]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.List[self.current+1] != None:
            return True
        else:
            return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].