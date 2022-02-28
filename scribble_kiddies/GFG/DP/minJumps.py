ans = []
def minJumps(A,cur,end,jumps):
    if cur >= end:
        ans.append(jumps)
        return ans
    for i in range(cur+1,cur+1+A[cur]):
        minJumps(A,i,end,jumps+1) 
A = [1,3,5,8,9,2,6,8,9]
A = [2 ,3, 1, 1, 2, 4, 2, 0, 1, 1]
print(ans)
print(minJumps(A,0,len(A)-1,0))
print(ans)

