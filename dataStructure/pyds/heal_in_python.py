#https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
#https://docs.python.org/3.0/library/heapq.html
#IMP Note :We uses heapq from python ref :https://docs.python.org/3/library/heapq.html
#It has only min heap. So to get max heap we will add - while insert and while reading, remove it

import heapq as hq

min_heap = list()
max_heap = list()

list1 = [2, 1, 5, 7, 2, 0, 5]

#1.heapify(list) : transform input list into min heap
mylist = [2, 1, 5, 7, 2, 0, 5]
print('before hippyfy, mylist:%r' %mylist)
hq.heapify(mylist)
#hq.heapify(max_heap,[-i for i in list1])
print('After hippyfy, mylist:%r' %mylist)

#2.heappush(list,value) : Push element to heap
#create empty list min_heap
min_heap = []
hq.heappush(min_heap, 5)
hq.heappush(min_heap, 2)
hq.heappush(min_heap, 3)
hq.heappush(min_heap, 1)
hq.heappush(min_heap, 4)
print('After heappush:%r' %min_heap)

#3.heappop(list) : Get top element from heap.It return with Deletion
v = hq.heappop(min_heap)
print('After heappop v:%r min_heap:%r ' %(v,min_heap))

#4.heappushpop(list) : 
#Push item on the heap, then pop and return the smallest item from the heap
#The combined action runs more efficiently than heappush() followed by a separate call to heappop().
v = hq.heappop(min_heap)
print('After heappop v:%r min_heap:%r ' %(v,min_heap))

#5.heapreplace()
#Pop and return the smallest item from the heap, and also push the new item. 
# The heap size doesnt change
#mylist = [2, 1, 5, 7, 2, 0, 5]
#hq.heapify(mylist)
print('before heapreplace', min_heap)
v = hq.heapreplace(min_heap,9)
print('After heapreplace', v,min_heap)


# ############################################
# before hippyfy, mylist:[2, 1, 5, 7, 2, 0, 5]
# After hippyfy, mylist:[0, 1, 2, 7, 2, 5, 5]
# After heappush:[1, 2, 3, 5, 4]
# After heappop v:1 min_heap:[2, 4, 3, 5]
# After heappop v:2 min_heap:[3, 4, 5]
# ('before heapreplace', [3, 4, 5])
# ('After heapreplace', 3, [4, 9, 5])
# ############################################


print("-----------MAX HEAP----------------")
#----MAX HEAP---
#how to create max heap using heapq?
# Just add -ve sign while reading and writing to/from heap

mylist = [2, 1, 5, 7, 2, 0, 5]
#change each element to negative and add
mylist2 = [-i for i in mylist]
print('before hippyfy, mylist:%r' %mylist2)
hq.heapify(mylist2)
#hq.heapify(max_heap,[-i for i in list1])
print('After hippyfy, MAX heap:%r' %mylist2)

#2.heappush(list,value) : Push element to heap

#create empty list max_heap

#While  writing Each element, add negative sign
max_heap = []
hq.heappush(max_heap, -5)
hq.heappush(max_heap, -2)
hq.heappush(max_heap, -3)
hq.heappush(max_heap, -1)
hq.heappush(max_heap, -4)

print('After heappush:%r' %max_heap)

#After reading add negative sign
v = - hq.heappop(max_heap)
print('After heappop v:%r min_heap:%r ' %(v,max_heap))
