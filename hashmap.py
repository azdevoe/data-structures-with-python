class hash:
    def __init__(self):
        self.arr = [None]*11
        
    def hasFunction(self,key):
        count = 0
        for s in key:
            count +=ord(s)-ord('a')
        return count%11
        
    def set(self,key,value):
        hashedKey=self.hasFunction(key)
        if self.arr[hashedKey] == None:
            self.arr[hashedKey] = [[key,value]]
        else:
                for i in range(len(self.arr[hashedKey])):
                    if self.arr[hashedKey][i][0] == key:
                        self.arr[hashedKey][i][1] = value
                        return
                self.arr[hashedKey].append([key,value])
    def get(self,key):
        idx = self.hasFunction(key)
        for i in range(len(self.arr[idx])):
            if self.arr[idx][i][0] == key:
                return self.arr[idx][i][1]
            
    def has(self,key):
        idx =self.hasFunction(key)
        if self.arr[idx] == None:
            return False
        for i in range(len(self.arr[idx])-1):
            if self.arr[idx][i][0] == key:
                return True
        return False
    
    def keys(self):
        keyArr=[]
        for bucket in self.arr:
            if bucket is not None:
                for inner in bucket:
                    keyArr.append(inner[0])
        return keyArr
    
    def values(self):
        keyArr=[]
        for bucket in self.arr:
            if bucket is not None:
                for inner in bucket:
                    keyArr.append(inner[1])
        return keyArr
    
    def delete(self,key):
        idx =self.hasFunction(key)
        
        for i in range(len(self.arr[idx]) ):
            if self.arr[idx][i][0] == key:
                self.arr[idx].pop(i)

        
v1 = hash()
v1.set('first',1)
v1.set('second',2)
v1.set('second',44)
v1.set('third',3)
v1.set('fourth',4)

print(v1.arr)
v1.delete('third')
print(v1.arr)