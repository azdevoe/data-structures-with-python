class PrefixSum:
    def __init__(self,arr):
        self.p = [0]*len(arr)
        self.p[0]=arr[0]
        for i in range(1,len(arr)):
            self.p[i]=self.p[i-1]+arr[i]
    def ps(self,f,s):
        if f ==0: return self.p[s]
        return self.p[s]-self.p[f-1]
n1=PrefixSum([3,5,6,7])
print(n1.ps(1,3))