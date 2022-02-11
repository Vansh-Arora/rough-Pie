arr = []
def create(nums,start,end):
    global arr
    if start > end:
        return None
    mid = (start + end) // 2
    arr.append(nums[mid])
    create(nums,start,mid-1)
    create(nums,mid+1,end)


create([1,2,3,4,5,6,7],0,6)
print(arr)

