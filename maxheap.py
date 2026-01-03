class maxHeap:
    def __init__(self):
        self.arr=[]
    def getParentIndex(self,index):
        return (index-1)//2
    def getLeftIndex(self,index):
        return (2*index)+1
    def getRightIndex(self,index):
        return (2*index)+2
    
    def getParent(self,index):
        return self.arr[self.getParentIndex(index)]
    def getLeftChild(self,index):
        return self.arr[self.getLeftIndex(index)]
    def getRightChild(self,index):
        return self.arr[self.getRightIndex(index)]
    def hasLeftChild(self,index):
        return self.getLeftIndex(index)<len(self.arr)
    def hasRightChild(self,index):
        return self.getRightIndex(index)<len(self.arr)
    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    
    def displayArr(self):
        return self.arr
    def swap(self,first,second):
        [self.arr[first],self.arr[second]]=[self.arr[second],self.arr[first]]
    
    def peak(self):
        if len(self.arr) == 0:
            return 'empty'
        return self.arr[0]
    
    def add(self,value):
        self.arr.append(value)
        self.heapifyUp()
    
    def removeTop(self):
        if len(self.arr) == 1:
            self.arr.pop()
            return
        [self.arr[0],self.arr[len(self.arr)-1]]=[self.arr[len(self.arr)-1],self.arr[0]]
        self.arr.pop()
        self.heapifyDown()
        
    def biggerChild(self,idx):
        if self.hasLeftChild(idx) and self.hasRightChild(idx):
            if self.getLeftChild(idx)>self.getRightChild(idx):
                return self.getLeftIndex(idx)
            else:
                return self.getRightIndex(idx)
        else:
            return self.getLeftIndex(idx)
    def heapifyUp(self):
        if len(self.arr) ==0:
            return 'empty'
        idx=len(self.arr)-1
        while self.hasParent(idx) and self.getParent(idx)<self.arr[idx]:
            self.swap(idx,self.getParentIndex(idx))
            idx=self.getParentIndex(idx)

    def heapifyDown(self):
        idx=0
       
        while self.hasLeftChild(idx):
            bigger=self.biggerChild(idx)
            if self.arr[idx]<self.arr[bigger]:
                self.swap(idx,bigger)
                idx=bigger
            else:
                break
mh=maxHeap()
mh.add(2)
mh.add(1)
mh.add(5)
mh.add(17)
mh.add(22)
mh.add(66)
mh.removeTop()
mh.removeTop()
mh.removeTop()
print(mh.peak())
print(mh.displayArr())