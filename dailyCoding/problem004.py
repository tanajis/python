# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time 
# and constant space. In other words, 
# find the lowest positive integer that does not exist in the array.
#  The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

#=============================================================================================
#!/usr/bin/env python
#title           :problem4.py
#description     :Geeksforgeeks Que and dailycoding
#author          :Tanaji Sutar
#date            :2020-Jan-30
#python_version  :2.7/3
#ref             :https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
#============================================================================================

"""
Approach:

if array size is 5. if all element between 1 to 5-->output will be 6
# if k number of elements are greater than size of Array 5.
# Ex.[2,3,1,6,7] here two elements 6 and 7 are above 5 size.
Hence we have chance of getting two numbers that are below five ( and >0) and are absent 
in given array.This is main idea behind the approach.

now for i in range(lenghofArray):[1,2,3,4,5]
    if i is between range 1 and 5(size) :
        it means we cant use i 
        hence in existing array only mark element whose index =i as negative
        Ex.if i ==3 , check 3 present in array
        if present mark element at index 3 as negative(whatever the value of element)
        (We are looking to mark just index here.value doesnt matter)

    In this way if array has elements 1,2,3 which are below size(5), 
    then values(whatever it may be) at indexes 1,2,3 will be marked as negative.

    now traverse our array again and find first index that has positive value.
    index number is the answer.    

"""

def segregate(arr,size): 
    j = 0
    for i in range(size): 
        if (arr[i] <= 0): 
            arr[i], arr[j] = arr[j], arr[i] 
            j += 1 # increment count of non-positive integers  
    print(arr)
    return j  
  
  
''' Find the smallest positive missing number  
in an array that contains all positive integers '''
def findMissingPositive(arr, size): 
    
    print('inside findMissingPositive',arr, size)
    # Mark arr[i] as visited by making arr[arr[i] - 1] negative.  
    # Note that 1 is subtracted because index start  
    # from 0 and positive numbers start from 1  
    for i in range(size): 
        print('firstloop:',i,arr[i],abs(arr[i]))
        print(arr)
        if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0):
            #if element is less than size and greater than 0 
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
            print('marking negetive',arr[abs(arr[i]) - 1],arr[i])
              
    # Return the first index value at which is positive  
    for i in range(size): 
        print('second loop:',i,arr,size)
        if (arr[i] > 0): 
              
            # 1 is added because indexes start from 0  
            return i + 1
    return size + 1
  
''' Find the smallest positive missing  
number in an array that contains  
both positive and negative integers '''
def findMissing(arr, size): 
      
    # First separate positive and negative numbers  
    shift = segregate(arr, size)
    print('shift',shift) 
      
    # Shift the array and call findMissingPositive for  
    # positive part  
    return findMissingPositive(arr[shift:], size - shift)  
      
# Driver code  
arr = [2, 3, 7, 6, 8, -1, -10, 15]
arr_size = len(arr)  
missing = findMissing(arr, arr_size)  
print("The smallest positive missing number is ", missing) 




"""
Approach from :https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
You are given an unsorted array with both positive and negative elements. You have to find the smallest positive number missing from the array in O(n) time using constant extra space. You can modify the original array.
Examples

 Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1

 Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
 Output: 4

 Input: {1, 1, 0, -1, -2}
 Output: 2 
Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
A naive method to solve this problem is to search all positive integers, starting from 1 in the given array. We may have to search at most n+1 numbers in the given array. So this solution takes O(n^2) in worst case.



 

We can use sorting to solve it in lesser time complexity. We can sort the array in O(nLogn) time. Once the array is sorted, then all we need to do is a linear scan of the array. So this approach takes O(nLogn + n) time which is O(nLogn).

We can also use hashing. We can build a hash table of all positive elements in the given array. Once the hash table is built. We can look in the hash table for all positive integers, starting from 1. As soon as we find a number which is not there in hash table, we return it. This approach may take O(n) time on average, but it requires O(n) extra space.

A O(n) time and O(1) extra space solution:
The idea is similar to this post. We use array elements as index. To mark presence of an element x, we change the value at the index x to negative. But this approach doesn’t work if there are non-positive (-ve and 0) numbers. So we segregate positive from negative numbers as first step and then apply the approach.

Following is the two step algorithm.
1) Segregate positive numbers from others i.e., move all non-positive numbers to left side. In the following code, segregate() function does this part.
2) Now we can ignore non-positive elements and consider only the part of array which contains all positive elements. We traverse the array containing all positive numbers and to mark presence of an element x, we change the sign of value at index x to negative. We traverse the array again and print the first index which has positive value. In the following code, findMissingPositive() function does this part. Note that in findMissingPositive, we have subtracted 1 from the values as indexes start from
 0 in C.
"""
