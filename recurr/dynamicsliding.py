def dynamic(arr,target):
    final=1000000000
    curr=start=0
    for end in range(len((arr))):
        curr=curr+arr[end]
        while curr>=target:
            final=min(final,end-start+1)
            curr-=arr[start]
            start+=1
    return final
print(dynamic([3,4,1,30,1,7],35))