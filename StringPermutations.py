import math
inStr = input()
ltrCount = {}
for ltr in inStr:
    if ltr in ltrCount:
        ltrCount[ltr] += 1
    else:
        ltrCount[ltr] = 1
ans = math.factorial(len(inStr))
for each in ltrCount.values():
    ans = ans//math.factorial(each)
print(ans)