class Solution:
    def convert(self, A, B):
        a = A
        A = []
        temp = ''
        for i in range(len(a)):
            if a[i] != '\n':
                temp += a[i]
            else:
                A.append(temp.strip())
                temp = ''
        A.append(temp.strip())
        size = -1
        for i in A:
            if len(i) > size:
                size = len(i)
        B = ['.' for i in range(size)]
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] != ".":
                    B[j] = A[i][j]
        ans  = ''
        for i in B:
            if i != ".":
                ans += i
        return (ans)	    
A = Solution()
print(A.convert("""P.......A........H.......N
       ..A..P....L....S....I...I....G
       ....Y.........I........R""",3))