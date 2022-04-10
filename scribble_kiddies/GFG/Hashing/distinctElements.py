def countE(A):
    dis = {}
    for i in A:
        if i not in dis:
            dis[i] = 0
    print(len(dis))

if __name__ == "__main__":
    countE([1,2,4,5,6,7,8,1,2,3,4,5,6,7,8])