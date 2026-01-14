def selection(arr):
    for i in range(len(arr)):
        minIdx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIdx]:
                minIdx=j
        [arr[minIdx],arr[i]]=[arr[i],arr[minIdx]]
    return arr
print(selection([6,5,7,3,9,55,1]))