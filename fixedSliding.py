def fixed(arr,size):
    final=-10000000
    curr = 0
    start=0
    
    for i in range(len(arr)):
        curr+=arr[i]
        if i>=size-1:
            final=max(curr,final)
            curr-=arr[start]
            start+=1
    return final

print(fixed([4,2,1,7,8,1,2,8,1,0],3))