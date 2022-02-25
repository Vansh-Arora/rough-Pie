def Treat(empty,i,A,B):
    wantedSlots = [A[i],B[i]]
    for j in wantedSlots:
        cur = empty[j]
        if empty[A[cur]] == -1:
            empty[A[cur]] = cur
            empty[j] = i
            return True
        elif empty[B[cur]] == -1:
            empty[B[cur]] = cur
            empty[j] = i
            return True 
    
def solution(A, B, S):
    # write your code in Python 3.6
    N = len(A)
    if N > S:
        return False
    else:
        slots = {}
        for i in range(1,S+1):
            slots[i] = []
        for i in range(N):
            slots[A[i]].append(i)
            slots[B[i]].append(i)
        print(slots)
        for i in range(1,S+1):
            if len(slots[i]) == 0:
                return False
    empty = [-1 for i in range(S)]
    treated = [0 for i in range(N)]
    for i in range(N):
        if empty[A[i]-1] == -1:
            empty[A[i]-1] = i
            treated[i] = 1
        elif empty[B[i]-1] == -1:
            empty[B[i]-1] = i
            treated[i] = 1
    print(empty,treated)
    i = 0
    while i < N:
        if not treated[i]:
            if Treat():
                i += 1
            else:
                return False
        else:
            i += 1
        

solution([1,1,3],[2,2,1],3)