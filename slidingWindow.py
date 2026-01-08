def sliding(arr):
    final = arr[0]
    curr = 0
    leftI,rightI=0,0
    L=0
    for R in range(len(arr)):
        if curr<0:
            curr=0
            L=R
        curr+=arr[R]
        
        if final<curr:
            final=curr
            leftI=L
            rightI=R
    return [leftI,rightI]

print(sliding([3,-1,-10,5,6]))
        