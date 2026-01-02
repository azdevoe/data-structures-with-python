def sort(arr):
    for i in range(len(arr)):
        minIdx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIdx]:
                minIdx=j
        [arr[minIdx],arr[i]] = [arr[i],arr[minIdx]]
    return arr

print(sort([5,6,3,4,2,9,1]))