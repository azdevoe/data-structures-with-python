class PrefixSum:
    def __init__(self,arr):
        self.arr=arr
        self.length=len(self.arr)
        self.p=[0]*self.length
        if self.arr==[]:return []
        self.p[0]=self.arr[0]
        for i in range(1,self.length):
            self.p[i] = self.p[i-1]+self.arr[i]
        print(self.p)

    def getSum(self,l,r):
        if l==0:return self.p[r]
        return self.p[r]-self.p[l-1]
    
yy= PrefixSum([8,3,-2,4,10,-1])
print(yy.getSum(0,1))