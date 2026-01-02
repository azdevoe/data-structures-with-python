class Singly:
    def __init__(self,value):
        self.data=value
        self.next = None
        
class Logic:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def push(self,value):
        newNode = Singly(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.length+=1
        
    def unshift(self,value):
        newNode=Singly(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.length+=1
    def display(self):
        arr=[]
        temp=self.head
        while temp:
            arr.append(temp.data)
            temp=temp.next
        return arr
    
    def pop(self):
        if self.length ==0:
            return
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            temp.next=None
            self.tail=temp
        self.length-=1
    
    def shift(self):
        if self.length ==0:
            return
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head.next
            self.head=temp
        self.length-=1
            
    def remove(self,index):
        if self.length==0 or index>self.length-1:
            return
        elif index==0 :
            return self.shift()
        elif index==self.length-1:
            return self.pop()
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            right=temp.next.next
            temp.next=right
            self.length-=1
            
    def reverse(self):
        if self.length==0:
            return None
        if self.length==1:
            return self.head
        prev,curr=None,self.head
        formerHead= self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev
        self.tail=formerHead
        return self.head
        
v2=Logic()
v2.push(5)
v2.push(6)
v2.unshift(1)
v2.unshift(3)
v2.unshift(4)
print(v2.display())
v2.reverse()
print(v2.display())