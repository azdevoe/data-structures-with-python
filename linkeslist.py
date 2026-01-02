class LinkedList:
    def __init__(self,node):
        self.node = node
        self.next = None
        
class Logic:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push(self,value):
        newNode = LinkedList(value)
        temp = self.head
        if not temp:
            self.head=newNode
            self.tail = newNode
            return
        self.tail.next=newNode
    
    def pop(self):
        temp = self.head
        while temp.next.next != None:
            temp=temp.next
        temp.next= None
    
    def display(self):
        temp= self.head
        arr=[]
        while temp:
            arr.append(temp.node)
            temp=temp.next
        return arr
    
    def addHead(self,value):
        newNode= LinkedList(value)
        temp = self.head
        newNode.next = temp
        self.head = newNode
        
    def removeHead(self):
        temp=self.head
        self.head=temp.next
        
    
v1=Logic()
v1.push(2)
v1.push(4)
v1.display()
print('-----------------')
v1.pop()
v1.display()
print("----------------")
v1.addHead(7)
v1.display()
print('---------------')
v1.removeHead()
v1.display()