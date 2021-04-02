class Solution:
    def countAndSay(self, A):
        start = '1'
        ans = []
        for i in range(A):
            if i == 0:
                ans.append(start)
            else:
                ans.append('')
                temp = ans[i-1][0]
                count = 0
                for j in ans[i-1]:
                    if j == temp:
                        count += 1
                    else:
                        ans[i] = ans[i] +( str(count) + temp)
                        temp = j
                        count = 1
                ans[i] = ans[i] +( str(count) + temp)
        return (ans)

A = Solution()
A.countAndSay(5)