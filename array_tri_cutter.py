arr = input().split()
arr = [int(i) for i in arr]
sum = 0
flag = 0
for i in arr:
    sum += i


i = 0
n = len(arr)
sby3 = 0
while i<n and sby3 < sum//3:
    sby3 += arr[i]
    i += 1

sby3 = sby3 - arr[i-1]
brk1 = i-1


temp = 0
while i < n and temp < sby3:
    temp += arr[i]
    if temp == sby3:
        flag = 1
        brk2 = i+1
        break
    i += 1

if flag == 1:
    i = brk2 + 1
    temp = 0
    while i < n:
        temp += arr[i]
        if temp > sby3:
            break
        i += 1
    if temp == sby3:
        print("True")
    else:
        print("False")
else:
    print("False")

