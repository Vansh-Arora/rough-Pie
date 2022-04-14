class Solution:
	# @param A : integer
	# @param B : integer
	# @return a strings
    def fractionToDecimal(self,A, B):
        if A == 0:
            return "0"
        if B == 0:
            return "N/A"
        if (A<0 and B<0) or (A>0 and B>0):
            flag = 0
        else:
            flag = 1
        A = abs(A)
        B = abs(B)
        whole = str(A//B)
        if flag:
            ans = "-"
        else:
            ans = ""
        ans += whole

        if A%B == 0:
            return ans
        ans += "."
        rem = A%B
        dis = {}
        ans2 = ""
        i = 0
        dis[rem] = i
        while rem != 0:
            rem *= 10
            ans2 += str(rem//B)
            i += 1
            rem %= B
            if rem in dis:
                idx = dis[rem]
                break
            else:
                dis[rem] = i
        if rem != 0:
            ans = ans + ans2[:idx] + '(' + ans2[idx:] + ')'
        else:
            ans += ans2
        return ans
