def lszero(A):
    sub = {}
    res = float("-inf")
    s = -1
    sm = 0
    e = -1
    for i in range(len(A)):
        sm += A[i]
        if sm == 0:
            sub[sm] = i
            if i+1 > res:
                res = i+1
                s = 0
                e = i
        elif sm in sub:
            if i-sub[sm] > res:
                res = i - sub[sm]
                s = sub[sm]+1
                e = i
        else:
            sub[sm] = i
    return A[s:e+1]


