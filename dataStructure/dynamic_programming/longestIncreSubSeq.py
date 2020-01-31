#=============================================================================================
#!/usr/bin/env python
#title           :longestIncreSubSeq.py
#description     :Longest increasing subsequence. Example of Dynamic prog without recursion
#                 Bottom up Approach and Memoization.No recursion
#author          :Tanaji Sutar
#date            :2020-Jan-31
#python_version  :2.7/3
#ref             :
#input           :[10,22,9,33,21,50,41,60]
#output          : 5  as longest Incr subseq will be either [10,22,33,50,60] or [10,22,33,41,60]
#Notes           :for given input [10,22,9,33,21,50,41,60]
                  #sequences are {10},{10,22},{22,10},{60,41,9,33}
                  #Increasing sequences are {10},{10,22},{22,33,50},{10,33,60},
                  #and [10,22,33,50,60],[10,22,33,41,60]
                  #longest are last and second last of above hence  max length is 5
#============================================================================================

def longIncrSubSeq(A):

    #create memo array/list of length as that of input Array.
    #set all value to 1 first
    n=len(A)
    memo=[1]*n
    #print(memo)

    #start j from 0 and i from 1(first & second index respectively)
    #range(2) gives [0,1]  
    for i in range(1,n,1):
        #i will be varying from 1 to (n-1)
        for j in range(0,i):
            #j will be from 0 to  (i-1)
            if A[i]>A[j] and memo[i]<(memo[j]+1):
                memo[i]=memo[j]+1
    
    #print(memo)
    return memo[n-1]


if __name__ == "__main__":
    A=[10,22,9,33,21,50,41,60]
    res=longIncrSubSeq(A)
    print('res:',res)

