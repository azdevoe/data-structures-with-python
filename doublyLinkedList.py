class doubly:
    def __init__(self,node):
        self.node=node
        self.next = None
        self.prev = None
        

class Logic:
    def __init__(self):
        self.head = None
        self.tail = None
        
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
    
    def addHead(self,value):
        newNode = doubly(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            temp = self.head
            newNode.next= temp
            self.head=newNode
        
    def pop(self):
        if self.head == None:
            return False
        else:
            temp = self.tail.prev
            temp.next = None
            self.tail.prev =None
            self.tail = temp
    def removeHead(self):
        temp=self.head.next
        temp.prev = None
        self.head.next=None
        self.head=temp
    def display(self):
        arr= []
        temp=self.head
        while temp:
            arr.append(temp.node)
            temp=temp.next
        return arr
v1 = Logic()
v1.addHead(1)
v1.addHead(2)
v1.push(4)
v1.push(5)
v1.addHead(1)
v1.pop()
v1.removeHead()
print(v1.display())
