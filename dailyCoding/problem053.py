https://www.geeksforgeeks.org/queue-using-stacks/

Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure
with the following methods: 
enqueue, which inserts an element into the queue, and dequeue, which removes it.


enQueue(q, x):

While stack1 is not empty, push everything from stack1 to stack2.
Push x to stack1 (assuming size of stacks is unlimited).
Push everything back to stack1.
Here time complexity will be O(n)

deQueue(q):

If stack1 is empty then error
Pop an item from stack1 and return it
Here time complexity will be O(1)


=======method2=====

enQueue(q,  x)
  1) Push x to stack1 (assuming size of stacks is unlimited).
Here time complexity will be O(1)

deQueue(q)
  1) If both stacks are empty then error.
  2) If stack2 is empty
       While stack1 is not empty, push everything from stack1 to stack2.
  3) Pop the element from stack2 and return it.
Here time complexity will be O(n)
