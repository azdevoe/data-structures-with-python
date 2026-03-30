def twoSum(arr,target):
    l=0
    r=len(arr)-1
    while r-l>0:
        if arr[r]+arr[l]> target:
            r-=1
        elif arr[r]+arr[l]< target:
            l+=1
        if arr[r]+arr[l]==target:
            return [l,r]
    return -1
print(twoSum([1,2,3,4,5,6],3))