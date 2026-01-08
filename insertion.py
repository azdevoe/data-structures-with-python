def insertion(arr):
    for i in range(1,len(arr)):
        value=arr[i]
        j=i-1
        while j>=0 and arr[j]>value:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=value
    return arr

print(insertion([4,5,2,7,1]))