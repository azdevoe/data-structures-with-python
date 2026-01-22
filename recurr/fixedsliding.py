def sliding(arr,sub):
    final=curr=sum(arr[:sub])
    for end in range(sub,len(arr)):
        curr=curr+arr[end]-arr[end-sub]
        final=max(final,curr)
    return final
print(sliding([3,4,1,77,8,4],3))