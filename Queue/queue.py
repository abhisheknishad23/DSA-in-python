class queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0
    
    def insert(self,value):
        self.items.append(value)

    def delete(self):
        if(self.isEmpty()):
            print('queue is empty')
        else:
            return self.items.pop(0)
        
q=queue()
q.insert(1)
q.insert(2)
q.insert(3)

print(q.delete())
print(q.delete())
print(q.delete())
q.delete()