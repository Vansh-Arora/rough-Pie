def romanToInt(A):
    ans = 0
    ROMANS = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
    n = len(A)
    for i in range(n-1):
        if ROMANS[A[i]] < ROMANS[A[i+1]]:
            ans -= ROMANS[A[i]]
        else:
            ans += ROMANS[A[i]]
    ans += ROMANS[A[n-1]]
    return ans



print(romanToInt('XXVII'))