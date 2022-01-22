def subsets(arr,n,i,osf):
    if i == n:
        print ('[' + osf + ']')
        return
    subsets(arr,n,i+1,osf)
    subsets(arr,n,i+1,osf+str(arr[i])+',')
subsets([1,2,3],3,0,'')   