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
    def hasRightChild(self):
        return
    def hasParent(self):
        return