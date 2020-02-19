###############################################################################
# problem 9 
# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?
###############################################################################

#=============================================================================================
#!/usr/bin/env python
#title           :problem9.py
#description     :DailyCoding #9
#author          :Tanaji Sutar
#date            :2020-feb-11
#python_version  :2.7/3
#ref             :
#============================================================================================

#A=[2, 4, 6, 2, 5]
#   0  1  2  3  4
def largestsumNonConsec(A,n,s):
    #print('called')
    #print(n,s)
    if n<0:
        #This condition add because in python index -1 goes to maximum index 
        return s

    #elif memo[n][s]
    elif n==0:
        #If only one element check if it is worth of adding or not
        #print('adding',A[n])
        r1=s+A[n]
        r2=s
        return max(r1,r2)
    else:
        #if A[n] include
        r1=largestsumNonConsec(A,n-2,s+A[n])
        #if A[n] excluded
        r2=largestsumNonConsec(A,n-1,s)
        return max(r1,r2)


if __name__ == "__main__":
    
    print('test case 1')
    A=[2, 4, 6, 2, 5]
    n=len(A)-1
    ans=largestsumNonConsec(A,n,0)
    print(ans)

    print('test case 2')
    A=[5, 1, 1, 5]
    n=len(A)-1
    ans=largestsumNonConsec(A,n,0)
    print(ans)
