###############
#This problem was asked by Uber.
#Given an array of integers, return a new array such that each element at index i 
#of the new array is the product of all the numbers in the original array except 
#the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output 
# would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
# the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?
#Ex.
#input [1, 2, 3, 4, 5]
#output [120, 60, 40, 30, 24]

#Note : complexity should be O(n) or less and Cant use devide.
################################################################################

#Solution designed By Tanaji Sutar spending 2-3 hrs. Say thanks to him first!!!!
#Date:29-01-2020

import math


def myAns(a):
    
    #If only two elements just swap them
    if len(a)==2:
        return [a[1],a[0]]
    elif len(a)==1:
        #If only one element return as it is
        return a

    l=[None]*len(a)
    r=[None]*len(a)
    k=[None]*len(a)

    m=math.ceil(len(a)/2)-1
    #print('med',m)
    min=0 
    max=len(a)-1 #in python index start at 0
    j=len(a)-1 # set j at last index of array
    f=m #f will have value from m to min with reduction of 1
    for i in range(len(a)):
        #print('loop',i)
        if i==0:
            l[i]=a[i]
            r[j]=a[j]
        else:
            l[i]=a[i]*l[i-1]
            r[j]=a[j]*r[j+1]
        j=j-1

        #Actuall value update will start here i=median.Here we will have left and right
        #    <--m-->  both way update of Array K
        #  
        if i>=m:
            
            #print('i',i,'f',f)
            
            if i<max:
                #update right part of Array k
                k[i]=l[i-1] * r[i+1]
            
            if f>min:
                #update left part of Array k
                k[f]=l[f-1] * r[f+1]
            
            elif i==max:
                #handle Extream end conditions min and max
                k[i]=l[i-1] # i is max here
                k[min]=r[min+1]

            
            #Ii will move left as per loop condition
            #move f towards left as below
            f=f-1

    #print(l)
    #print(r)
    #print(k)
    return k
    
    

if __name__ == "__main__":
    

    print('test 1:')
    a=[1, 2, 3, 4, 5]
    print('Input Array:',a)
    res=myAns(a)
    print('Output Array:',res)
    

    print('test 2:')
    a=[10, 20,30]
    print('Input Array:',a)
    res=myAns(a)
    print('Output Array:',res)


    print('test 3:')
    a=[8,14]
    print('Input Array:',a)
    res=myAns(a)
    print('Output Array:',res)

    print('test 4:')
    a=[1,2,3,4,5,6]
    print('Input Array:',a)
    res=myAns(a)
    print('Output Array:',res)
