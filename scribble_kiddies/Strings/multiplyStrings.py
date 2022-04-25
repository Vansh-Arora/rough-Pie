def add(A,B):
    ans = ''
    n = len(A)
    m = len(B)
    if n == 0:
        return B
    if m == 0:
        return A
    i = n-1
    j = m-1
    carry = 0
    while i > -1 and j > -1:
        tmp = int(A[i]) + int(B[j])
        tmp += carry
        tmp = str(tmp)
        if len(tmp) == 2:
            carry = int(tmp[0])
        else: carry = 0
        temp = tmp[-1]
        ans = temp + ans
        i -= 1
        j -= 1

    while i > -1:
        temp = str(int(A[i]) + carry)
        if len(temp) == 2:
            carry = int(temp[0])
        else:
            carry = 0
        tmp = temp[-1]
        ans = tmp + ans
        i -= 1
    while j > -1:
        temp = str(int(B[j]) + carry)
        if len(temp) == 2:
            carry = int(temp[0])
        else:
            carry = 0
        tmp = temp[-1]
        ans = tmp + ans
        j -= 1
    if carry > 0:
        return str(carry) + ans
    return ans
    
def multiply(A, B):
    multiplier = ''
    nB = len(B)
    nA = len(A)
    ans = ''
    for i in range(nB-1,-1,-1):
        temp = ''
        carry = 0
        for j in range(nA-1,-1,-1):
            tmp = int(A[j]) * int(B[i])

            tmp += carry
            tmp = str(tmp)

            if len(tmp) == 2:
                carry = int(tmp[0])
            else: carry = 0

            temp = tmp[-1] + temp
        if carry > 0:
            temp = str(carry) + temp
        temp += multiplier
        ans = add(ans,temp)
        multiplier += '0'
    zeroes = 0
    for i in range(len(ans)-1):
        print(ans)
        if ans[i] == '0':
            zeroes += 1
        else:
            break
    if zeroes != -1:
        return ans[zeroes:]
    return ans

print(multiply('00025','4'))