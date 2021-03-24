class Solution:
    # @param A : list of integers
    # @param B : integer length
    # @param C : integer max + 1
    # @return an integer
    def solve(self, A, B, C):
        n = len(str(C))
        array_size = len(A)

        if array_size == 0:
            ans = 0
        
        elif n < B:
            ans = 0
        
        elif n > B:
            if 0 in A:
                ans = (array_size - 1) * (array_size ** (B-1))
            else:
                ans = array_size ** B
        
        else:
            dig_array = [int(i) for i in str(C)]
            ans = 0
            for i in range(n):
                if i == 0:
                    temp = 0
                    j = 0
                    if 0 in A:
                        while(j < array_size and A[j] < dig_array[i]):
                            temp += 1
                            j += 1
                        ans += (temp - 1) * (array_size ** (n-1))
                        #print(ans)
                    else:
                        while(j < array_size and A[j] < dig_array[i]):
                            temp += 1
                            j += 1
                        ans += (temp) * (array_size ** (n-1))
                    #if ans == 0:
                       # break
                    if dig_array[i] not in A:
                        break
                else:
                    temp = 0
                    j = 0
                    while(j < array_size and A[j] < dig_array[i]):
                        temp += 1
                        j += 1
                    ans += temp *  (array_size**(n-i-1))
                    if dig_array[i] not in A:
                        break
        if B == 1 and 0 in A:
            ans += 1
        return ans
                    

a = Solution()

ans = a.solve([0,1,2,5],2,21)
print(ans)
                        
                        
                        
                        