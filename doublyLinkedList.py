class doubly:
    def __init__(self,node):
        self.node=node
        self.next = None
        self.prev = None
        

class Logic:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length=0

        
    def push(self,value):
        newNode = doubly(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            tailP = self.tail
            newNode.prev = tailP
            self.tail.next=newNode
            self.tail = newNode
        self.length+=1
    
    def addHead(self,value):
        newNode = doubly(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            temp = self.head
            newNode.next= temp
            temp.prev=newNode
            self.head=newNode
        self.length+=1
        
    def pop(self):
        if self.head == None:
            return False
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            temp = self.tail.prev
            temp.next = None
            self.tail.prev =None
            self.tail = temp
        self.length-=1
        return True
    def removeHead(self):
        if self.length==0:
            return False
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head.next
            temp.prev = None
            self.head.next=None
            self.head=temp
        self.length-=1
        return True
    def display(self):
        arr= []
        temp=self.head
        while temp:
            arr.append(temp.node)
            temp=temp.next
        return arr
    
    def find(self,index):
        temp = self.head
        count=0
        if index<0:
            return -1
        while temp:
            if count == index:
                return temp.node
            temp=temp.next
            count+=1
        return -1
    
    def delete(self,index):
        print('the len is ',self.length)
        if index <0 or index>=self.length:
            return False
        if index==0:
            return self.removeHead()
        if index==self.length-1:
            return self.pop()
        temp=self.head
        for _ in range(index):
            temp=temp.next
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
    
        self.length -= 1
        return True
        
                
                
v1 = Logic()
v1.addHead(1)
v1.addHead(2)
v1.push(4)
v1.push(5)
v1.addHead(1)
v1.pop()
v1.removeHead()
print(v1.display())
print(v1.find(5))
print(v1.delete(1))
print(v1.display())