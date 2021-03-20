class Solution:
    def BubbleSort(elements,A):
        n = len(elements)
        for i in range(n):
            for j in range(n-i-1):
                if elements[j]>elements[j+1]:
                    elements[j],elements[j+1] = elements[j+1],elements[j]
                    A[j],A[j+1] = A[j+1],A[j]
    
    def largestNumber(self, A):
        #A = [3, 30, 34, 5, 9, 50]
        ans = ''
        M = max(A)
        max_len = len(str(M))

        num = [str(i) for i in A]
        num2 = [str(i) for i in A]
        for i in range(len(num)):
            if len(num[i]) < max_len:
                num[i] += num[i][-1] * (max_len-len(num[i]))
        self.BubbleSort(num,num2)
        num2.reverse()
        for i in num2:
            ans = ans + i
        return (ans)