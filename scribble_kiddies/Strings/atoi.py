def atoi(A):
    s = 0
    n = len(A)
    flag = 0
    count = 0
    if A[0] == '+':
        s = 1
        flag = 0
        count = 1
    elif A[0] == '-':
        s = 1
        flag = 1
        count = 1
    
    for i in range(s,len(A)):
        if ord(A[i]) not in range(48,58):
            break
        else:
            count += 1
    if count == s:
        return 0

    ans = int(A[s:count])
    if ans > 2**31:
        if flag:
            return -2**31
        return 2**31-1

    if flag: return -ans
    return ans