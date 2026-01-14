def sliding(arr,fixed):
    if fixed>len(arr): return 'stop'
    final=curr=sum(arr[:fixed])
    for i in range(fixed,len(arr)):
        curr=curr+arr[i]-arr[i-fixed]
        final=max(curr,final)
    return final


print(sliding([9,2,4,-50,8],3))
# def sliding(arr,target):
#     curr=0
#     final=1000000000
#     start=0
#     for end in range(len(arr)):
#         curr+=arr[end]
#         while curr>=target:
#             curr-=arr[start]
#             final=min(final,end-start+1)
#             start+=1
#     return final
            
