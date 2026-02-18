# implement a queye using two stacks python

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue operation
        self.stack2 = []  # For dequeue operation

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            # Transfer elements from stack1 to stack2, reversing order
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            raise IndexError("dequeue from empty queue")

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]
        else:
            raise IndexError("peek from empty queue")


# q = QueueUsingStacks()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# print(q.dequeue())  # Output: 10
# print(q.peek())     # Output: 20
# print(q.dequeue())  # Output: 20
# print(q.is_empty()) # Output: False