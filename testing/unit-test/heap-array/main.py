from tms_pyds import heap_array

if __name__ == "__main__":

    #create a min heap using array or list of integers
    minheap = heap_array.Heap()
    array = [3,2,5,3,7,8]
    minheap.hippify(array)
    
    #show heap
    minheap.show()

    min_element = minheap.heapPop()
    print('Minimun number using heapPop:%r' % min_element)

    print('Push element t heap')
    minheap.heapPush(-10)
    minheap.show()

    
