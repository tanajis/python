class stackNode:
    def __init__(self,next):
        self.data=data
        self.next=next

class stack():
    def __init__(self):
        stackTop=None
    
    def push(self,data):
        if self.stackTop is None:
            self.stackTop=stackNode(data,None)
        else:
            temp =self.stackTop
            newNode=stackNode(data,temp.data)
            self.stackTop=newNode
    
    def pop(self)
            

