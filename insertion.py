def insertion(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            former=arr[j-1]
            if arr[j-1]>arr[j]:
                arr[j]=arr[j-1]
                arr[j-1]=former
    return arr

print(insertion([5,6,3,4,2,9,1]))