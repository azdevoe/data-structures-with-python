
class heap:
    def __init__(self):
        self.arr = []
    
    def getParentIndex(self,index):
        return ((index-1)//2)
    
    def getLeftChildIndex(self,index):
        return (2*index)+1
    
    def getRightChildIndex(self,index):
        return (2*index)+2
    
    def hasLeftElement(self,index):
        return self.getLeftChildIndex(index)<len(self.arr)
    def hasRightElement(self,index):
        return self.getRightChildIndex(index)<len(self.arr)
    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    
    def getLeftChild(self,index):
        return self.arr[self.getLeftChildIndex(index)]
    def getRightChild(self,index):
        return self.arr[self.getRightChildIndex(index)]
    def getParent(self,index):
        return self.arr[self.getParentIndex(index)]
    def getArr(self):
        return self.arr
    
    def swap(self,first,second):
        [self.arr[first],self.arr[second]] =[self.arr[second],self.arr[first]]
    
    def peek(self):
        if len(self.arr) ==0:
            return 'empty'
        self.arr[0]
    def removeTop(self):
        if len(self.arr) ==0:
            return 'empty'
        [self.arr[0],self.arr[len(self.arr)-1]] =[self.arr[len(self.arr)-1],self.arr[0]]
        self.heapifyDown()
        return
    
    def add(self,value):
        self.arr.append(value)
        self.heapifyUp()
        
    def heapifyUp(self):
        index = len(self.arr)-1
        while self.hasParent(index) and self.getParent(index)>self.arr[index]:
            self.swap(self.getParentIndex(index),index)
            index=self.getParentIndex(index)
        
    def heapifyDown(self):
        index=0
        while self.hasLeftElement(index):
            smaller=self.getLeftChildIndex(index)
            if self.hasRightElement(index) and self.getRightChild(index)<smaller:
                smaller=self.getRightChildIndex(index)
            if self.arr[index]<self.arr[smaller]:
                break
            self.swap(index,smaller)
            index=smaller
        self.arr.pop()
            
v1 =heap()
v1.add(3)
v1.add(2)
v1.add(1)
v1.removeTop()
print(v1.getArr())