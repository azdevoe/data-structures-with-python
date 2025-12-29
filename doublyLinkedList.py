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
            return
        else:
            tailP = self.tail
            newNode.prev = tailP
            self.tail.next=newNode
            self.tail = newNode
    
    def addHead(self,value):
        newNode = doubly(value)
        temp = self.head
        newNode.next= temp
        self.head=newNode
    def display(self):
        arr= []
        temp=self.head
        while temp:
            arr.append(temp.node)
            temp=temp.next
        return arr
v1 = Logic()
v1.push(4)
v1.push(5)
v1.addHead(1)
print(v1.display())
