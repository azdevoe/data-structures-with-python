def sliding(arr,target):
    final=100000000
    start= curr=0
    
    for end in range(len(arr)):
        curr+=arr[end]
        while curr>=target:
            final = min(final,end-start+1)
            curr-=arr[start]
            start+=1
    return final

print(sliding([5,6,6],11))


#for negative we use prefix sum and a dequeue

# def sliding(arr):
#     final = arr[0]
#     curr = 0
#     leftI,rightI=0,0
#     L=0
#     for R in range(len(arr)):
#         if curr<0:
#             curr=0
#             L=R
#         curr+=arr[R]
        
#         if final<curr:
#             final=curr
#             leftI=L
#             rightI=R
#     return [leftI,rightI]

# print(sliding([3,-1,-10,5,6]))
#this is for kadane