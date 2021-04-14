test = int(input())
A = []
for i in range(test):
    ans  = 0
    r,g,b = input().split()
    r = int(r)
    g = int(g)
    b = int(b)
    mn = min(r,g,b)
    mx = max(r,g,b)
    mid = r+g+b-(mn+mx)
    if((mx-mn) >= mid ):
        ans=mn
        mx=mx-mn
        mn=0
        print(mx)
    else:
        ans=mx-mid
        mn=mn-ans
        mx=mx-ans
        if(mn%2==0):
            ans=mn+ans
            mx=mx-mn//2
            mid=mid-mn//2
        else:
            ans=mn+ans
            mx=mx-(mn//2)-1
            mid=mid-mn//2
    
    ans=ans+min(mid,mx)
    print(ans)

