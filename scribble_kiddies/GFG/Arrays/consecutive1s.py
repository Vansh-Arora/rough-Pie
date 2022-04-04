def get(A):
    res = float("-inf")
    count = 0
    for i in A:
        if i == 1:
            count += 1
            if count > res:
                res = count
        else:
            count = 0
    return res

if __name__ == "__main__":
    A = [0,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1]
    ans = get(A)
    print(ans)