class Dequeue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0
    
    def insertAtEnd(self,value):
        self.items.append(value)

    def deleteFront(self):
        if(self.isEmpty()):
            print('queue is empty')
        else:
            return self.items.pop(0)
        
    def insertAtFront(self,value):
        self.items.insert(0,value)

    def deleteEnd(self):
        if(self.isEmpty()):
            print('Queue is empty')
        else:
            return self.items.pop()
        
dq=Dequeue()
dq.insertAtEnd(1)
dq.insertAtFront(2)
dq.insertAtEnd(3)
dq.insertAtEnd(4)
dq.insertAtFront(5)

print(dq.deleteEnd())
print(dq.deleteEnd())
print(dq.deleteFront())
print(dq.deleteFront())
print(dq.deleteEnd())
dq.deleteEnd()
dq.deleteFront()