def binary(arr,target):
    l,r=0,len(arr)
    while r-1>1:
        mid = l+(r-l)//2
        if mid>target:
            r=mid
        else:
            l=mid
            
    return l
print(binary([1,2,3,4,5,6,7]),5)