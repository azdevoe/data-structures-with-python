def kadane(arr):
    final=arr[0]
    curr=0
    for num in arr:
        curr=max(curr,0)
        curr+=num
        final=max(final,curr)
    return final
print(kadane([2,4,-50,8]))