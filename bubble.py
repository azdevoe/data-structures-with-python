def bubble(arr):
    for i in range(len(arr)):
        j=i
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                [arr[j],arr[j+1]]=[arr[j+1],arr[j]]
    return arr
    
print(bubble([4,5,2,7,1]))