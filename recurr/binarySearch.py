def binarySearch(arr,target):
    l,r=0,len(arr)
    while r-l>1:
        mid=l+(r-l)//2
        if arr[mid]>target:
            r=mid
        else:
            l=mid
    if arr[l] != target:
        return -1
    return l

print(binarySearch([1,2,3,4,5,6,7,8,9,10,11],7))