def kadane(arr):
    final=arr[0]
    curr=-77777777
    L=0
    ml,mr=0,0
    for R in range(len(arr)):
        curr+=arr[R]
        if curr<=0:
            L=R
            curr= 0
        if curr>final:
            final=curr
            ml,mr=L,R
    return [final,ml,mr]

print(kadane([-101,-2,-1,-14]))
        





















# def kadane(arr):
#     final=arr[0]
#     curr=0
#     for num in arr:
#         curr = max(0,curr)
#         curr+=num
#         final=max(curr,final)
#     return [final]

# print(kadane([-101,-2,-1,-14]))