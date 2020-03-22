# This problem was asked by Microsoft.
# Compute the running median of a sequence of numbers. That is, given a stream of 
# numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2
#=============================================================================================
#!/usr/bin/env python
#title           :problem033.py
#description     :runing Median of integer stream  #DailyCoding.Application of HEAP data structure
#author          :Tanaji Sutar
#date            :2020-Mar-22
#python_version  :2.7/3  
#============================================================================================


#IMP:
#median is middle number in ORDERED ODD LIST
#median is eman of two middle numbers in ORDERED EVEN LIST
#[2] -->2
#[2,1]-->ordered[1,2]-->ODD so 1+2/2 =1.5
#[2,1,5]-->ordered[1,2,5]-->ODD hence median is 2
#[2,1,5,7]-->ordered[1,2,5,7]-->EVEN  so 2+5 /2 ==3.5
#[2,1,5,7,2]-->ordered[1,2,2,5,7]-->ODD hence median is 2
#[2,1,5,7,2,0]-->ordered[0,1,2,2,5,7]-->EVEN hence median is 2+2/2 =2
#[2,1,5,7,2,0,5]-->ordered[0,1,2,2,5,5,7]-->ODD hence 2


#refer :https://www.geeksforgeeks.org/median-of-stream-of-running-integers-using-stl/
#
#-------------Algorithm ------:
#
# Create two heaps. max heap:lower half(Left side) and one min heap: higher half(right side).
# Take initial value of median as 0.
# For every newly read element, insert it into either max heap or min heap and calculate the median based on the following conditions:
# If the size of left  > size of right 
#   IF the element is less than previous median: 
#       pop top from max & move into min heap 
#       insert the new element to max heap 
#   else 
#       insert the new element to min heap. 
# new median = average of top of both heap.
# 
# 
# If the size of max heap < size of min heap 
#   IF the element is greater than previous median:
#       pop from min heap and insert into max 
#       insert the new element to min heap 
#   else 
#       insert the new element to max heap. 
# 
# new median = average of top of both heap.
# 
# 
# If the size of max heap  == size of min heap 
#   if current is less than previous median:
#       insert it to max heap 
#       new median = top element of max heap. 
#    If the current element is greater than previous median 
#       insert it to min heap 
#       new median = top element of min heap.

#Demonstration:
#Intially max and min  heap are empty
# ('x', 2, 'prev_med', 0, 'max_heap(L)', [], 'min_heap(R)', [2])
# ('x', 1, 'prev_med', 2, 'max_heap(L)', [-1], 'min_heap(R)', [2])
# ('x', 5, 'prev_med', 1.5, 'max_heap(L)', [-1], 'min_heap(R)', [2, 5])
# ('x', 7, 'prev_med', 2, 'max_heap(L)', [-2, -1], 'min_heap(R)', [5, 7])
# ('x', 2, 'prev_med', 3.5, 'max_heap(L)', [-2, -1, -2], 'min_heap(R)', [5, 7])
# ('x', 0, 'prev_med', 2, 'max_heap(L)', [-2, -1, 0], 'min_heap(R)', [2, 7, 5])
# ('x', 5, 'prev_med', 2.0, 'max_heap(L)', [-2, -1, 0], 'min_heap(R)', [2, 5, 5, 7])

#IMP Note :We uses heapq from python ref :https://docs.python.org/3/library/heapq.html
#It has only min heap. So to get max heap we will add - while insert and while reading, remove it

import heapq as hq

def get_running_medians(arr):
    if not arr:
        return None

    #Create 2 heaps

    #min_heap for upper half(right side) 
    min_heap = list()

    #max_heap for lower half (left side)
    max_heap = list()
    medians = list()

    prev_med = 0
    med = None
    for x in arr:
        if med is not None:
            prev_med = med
        
        if len(max_heap) > len(min_heap) :
            #left has more elements than right

            if x < prev_med:
                
                #If new element is less reater than previous median
                #So ideally it should go to left,but we cant insert directly (as left >right)
                #we need to perform balancing before inserting to left

                #remove from left(maxheap so add negative)
                top_element = - hq.heappop(max_heap)
                #max_heap.pop(0)
                
                #add it to right
                hq.heappush(min_heap, top_element)

                #After balancing add new element to left(maxheap so add negative)
                hq.heappush(max_heap, -x)

            else:
                #even though left has more element than right but new element is 
                # greater than previous So ideally it is going in the right.
                # So no need of balancing, directly push to right

                hq.heappush(min_heap, x)
            
            #Now calculate median(maxheap so add negative)
            med = (min_heap[0] + (-max_heap[0])) / 2.0


        elif len(min_heap) > len(max_heap) :
            #Right has more elements than left

            if x > prev_med:
                #new element is greater than previous median
                #So ideally it should go to right,but we cant insert directly(as right>left)
                #we need to perform balancing before inserting to right

                #remove from right
                top_element = hq.heappop(min_heap)
                
                #add to left(maxheap so add negative)
                hq.heappush(max_heap, -top_element)

                #After balancing add new element to right
                hq.heappush(min_heap, x)

            else:
                #even though right has more element than left but new element is less than previous
                #So ideally it is going in the left.So no need of balancing, directly push to left
                #(maxheap so add negative sign)
                hq.heappush(max_heap, -x)
            
            #Now calculate median (maxheap so add negative sign)
            med = (min_heap[0] + (-max_heap[0])) / 2.0

        
        else:
            #left and right has same length

            if x < prev_med:
                # New element is less than previous, needs to be added to left#(maxheap so add negative sign)
                hq.heappush(max_heap, -x)
                #mediun will be top of left (maxheap so add negative sign)
                med = -max_heap[0] 

            else:
                # New element is greater than previous, needs to be added to right
                hq.heappush(min_heap, x)
                #mediun will be top of right
                med = min_heap[0] 
            
            
        medians.append(med)
        #print('x',x,'prev_med',prev_med,'max_heap(L)',max_heap,'min_heap(R)',min_heap)

    return medians

"""
assert not get_running_medians(None)
assert not get_running_medians([])
assert get_running_medians([2, 5]) == [2, 3.5]
assert get_running_medians([3, 3, 3, 3]) == [3, 3, 3, 3]
assert get_running_medians([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
"""
print(get_running_medians([2, 1, 5, 7, 2, 0, 5]))

assert get_running_medians([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2.0, 2]
