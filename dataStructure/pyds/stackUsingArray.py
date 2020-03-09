
#IMP python list has all featires of stack. We can use it as stack



class stackUsingArray:
    def __init__(self):
        self.stk=[]

    def push(self,data):
        self.stk.append(data)
        print('Push Operation:%s is added to stack' %str(data))
    
    def pop(self):
        data=self.stk[-1]
        self.stk.pop(-1)
        print('Pop operation :%s is removed from stack' %str(data))
        
    def isEmpty(self):
        if self.stk is None:
            return True

        if len(self.stk)==0:
            return True
        else:
            return False
    def peek(self):
        return self.stk[-1]

    def showStack(self):
        print(self.stk)


if __name__ == "__main__":
    
    #create Stack
    mystack1=stackUsingArray()

    #check if it is an empty
    print('Is stack Empty?:%s' %str(mystack1.isEmpty()))

    #push data to stack
    mystack1.push('tanaji')

    #check if it is an empty
    print('Is stack Empty?:%s' %str(mystack1.isEmpty()))
    
    #push ore data to stack
    mystack1.push('pankaj')
    mystack1.push('sumit')

    mystack1.showStack()
    #pop data from stack
    mystack1.pop()
    mystack1.showStack()

