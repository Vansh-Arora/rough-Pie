class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        que = []
        ans = ''
        alpha = [0 for i in range(26)]
        for i in A:
            if alpha[ord(i)-97] == 0:
                que.append(i)
                alpha[ord(i)-97] += 1

            else:
                if alpha[ord(i)-97] == 1:
                    que.remove(i)
                alpha[ord(i)-97] += 1
                

            if len(que) != 0:
                ans += que[0]
            else:
                ans += '#'
        return ans
A = Solution()
print(A.solve('jpxvxivxkkthvpqhhhjuzhkegnzqriokhsgea'))
