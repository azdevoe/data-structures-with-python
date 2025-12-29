ll=[]
ll




def ad(arr,target):
    mapper={}
    for i in range(len(arr)):
        res= int(target)-arr[i]
        if res in mapper.keys():
            return [i,mapper.get(res)]
        mapper[arr[i]] = i
        
print(ad([1,2,3,4],6))