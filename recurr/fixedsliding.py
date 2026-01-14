def sliding(arr,sub):
    final = curr= sum(arr[:sub])
    for i in range(sub,len(arr)):
        curr = curr+arr[i]-arr[i-sub]
        final = max(final,curr)
    return final
    
print(sliding([3,4,1,77,8,4],3))