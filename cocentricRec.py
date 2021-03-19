'''
class Solution:
    def prettyPrint(self, A):
        for i in range(((2*A)-1)):
            for j in range(((2*A)-1)):
                if i < A and j < A:
                    print(max(A-i, A-j))
                elif i < A and j > A:
                    print(max(A-i,A-((2*A) - 2)+j))
                elif i >= A and j < A:
                    print(max(A-((2*A) - 2)+i,A-j))
                elif i >= A and j > A:
                    print(max(A-((2*A) - 2)+i,A-((2*A) - 2)+j))
            print()
'''
class Solution:
    def prettyPrint(self, A):
        ans = []
        for i in range(((2*A)-1)):
            ans.append([])
            for j in range(((2*A)-1)):
                if i < A and j < A:
                    ans[i].append(max(A-i, A-j))
                elif i < A and j >= A:
                    ans[i].append(max(A-i,A-((2*A) - 2)+j))
                elif i >= A and j < A:
                    ans[i].append(max(A-((2*A) - 2)+i,A-j))
                elif i >= A and j >= A:
                    ans[i].append(max(A-((2*A) - 2)+i,A-((2*A) - 2)+j))
        return ans
A = Solution()
print(A.prettyPrint(4))
