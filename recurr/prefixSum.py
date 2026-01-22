class PrefixSum:
    def __init__(self,arr):
        self.p = [0]*len(arr)
        self.p[0]=arr[0]
        for i in range(1,len(arr)):
            self.p[i]=self.p[i-1]+arr[i]
    def ps(self,l,r):
        if l==0: return self.p[r]
        return self.p[r]-self.p[l-1]
n1=PrefixSum([1,2,3,4,5])
print(n1.ps(1,3))