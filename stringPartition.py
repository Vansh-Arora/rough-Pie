def part(s):
    A = []
    n = len(s)
    dis = 0
    for i in s:
        if i not in A:
            dis += 1
            A.append(i)
    while dis > 0:
        A = []
        dis2 = 0
        i = 0
        while i < n:
            if s[i] not in A:
                dis2 += 1
                A.append(s[i]) 
                if dis2 == dis:
                    break 
            i += 1
        dis3 = 0
        A = []
        while i < n:
            if s[i] not in A:
                dis3 += 1
                A.append(s[i])
                if dis3 == dis:
                    break
            i += 1
        if dis2 == dis3:
            return dis2
        else:
            dis -= 1
    return dis


if __name__ == '__main__':
    s = 'aabbca'
    print(part(s))