# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the
#  array, compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should
#  get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array
# in-place and you do not need to store the results. You can simply
# print them out as you compute them.


#Note : this we need to do in O(n).Only one for loop,only one iteration of g8iven Array


from collections import deque


def get_sliding_max(a, k):

    window_max_elements = list()

    if not a:
        return None
    if len(a) <= k:
        return max(a)

    dq = deque()


    max=None
    res=[]
    for i in range(k):
        if max is None:
            max=a[i]
        else:
            if max< a[i]:
                max=a[i]

        dq.append(i)
    res.append(max)

    print('hi',dq,res)

    
    for i in range(k,len(a)):
        print('i',i,dq)

        #if i =3 Remove those indexes 0 as we need 1,2,3 now
        while dq and dq[0] <= i - k:
            dq.popleft()
            print('popleft',dq)
        
        #from end , remove every element from dq which is less that curr
        while dq and a[dq[-1]] < a[i]:
            dq.pop()
            print('pop',dq)

        dq.append(i)
        res.append(a[dq[0]])
    

    print(res)


    print(window_max_elements)
    return window_max_elements


print(get_sliding_max([10, 5, 2, 7, 8, 7], 3))
#assert get_sliding_max([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
#assert get_sliding_max([5, 2, 1], 2) == [5, 2]



#10, 5, 2, 7, 8, 7],

#i=2   0,1,2
#i=3   3-3=0 remove 0  -->[1,2] and append 3 -->[1,2,3]   popleft 1:a[1]>a[3] keep a[1] at zero index as it is.   pop: a[3] is 7 henec pop(from right) remove all that is less than 7(remove 1 & 2 and add 3) .Thus dq=[3]
#i=4   4-3=1 remove 1  -->[2,3] and append 4 -->[2,3,4]   popleft nothing . a[4]=8 . henece remove all that is less (3) and append 4 at the end Thus dq=[4]
#i=5   5-3=2 remove 2  -->[3,4] and append 5 -->[3,4,5]   popleft 3 .dq=[] Now  a[i]=7. 

