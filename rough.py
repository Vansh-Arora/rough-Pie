import sys
n,k = sys.stdin.readline().split()
n = int(n)
k = int(k)
s = sys.stdin.readline()
used = [0 for i in range(n)]
st = []
count = 0
for i in range(n):
    if s[i] == '(':
        st.append(i)
    elif s[i] == ')':
        used[st[-1]] = 1
        used[i] = 1
        st.pop()
        count += 2
        if count == k:
            break
ans = ''
for i in range(n):
    if used[i] == 1:
        ans += s[i]
print(ans)
