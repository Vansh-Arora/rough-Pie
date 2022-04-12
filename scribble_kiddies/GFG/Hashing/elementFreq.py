def frequency(A):
    freq = {}
    for i in A:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print(freq)

if __name__ == "__main__":
    frequency([1,2,4,5,6,7,8,1,2,3,4,5,6,7,8])