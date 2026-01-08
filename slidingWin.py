def sliding(arr,target):
    curr=0
    final=1000000000
    start=0
    for end in range(len(arr)):
        curr+=arr[end]
        while curr>=target:
            curr-=arr[start]
            final=min(final,end-start+1)
            start+=1
    return final
            
print(sliding([4,2,2,7,8,1,2,8,10],20))