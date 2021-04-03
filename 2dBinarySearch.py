class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def binarySearch(self,A,target):
        start = 0
        n = len(A)
        end = n-1
        while start <= end:
            mid = (start+end)//2
            if A[mid] == target:
                return mid
            elif A[mid]<target:
                start = mid+1
            else:
                end = mid-1
        return -1
                
    def searchMatrix(self, A, B):
        start = 0
        end = len(A) - 1
        while start < end:
            mid = (start + end)//2
            if A[mid][0] <= B:
                if B <= A[mid][-1]:
                    start = mid
                    break
                start = mid + 1
            else:
                end = mid - 1
        if self.binarySearch(A[start],B) != -1:
            return 1
        return 0
        