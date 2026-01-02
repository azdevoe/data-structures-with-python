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
        