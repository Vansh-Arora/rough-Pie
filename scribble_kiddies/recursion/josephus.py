def kill(n,k):
    if n == 1:
        return 0
    return (kill(n-1,k)+k)%n

print(kill(7,3))