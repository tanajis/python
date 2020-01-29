#=============================================================================================
#!/usr/bin/env python
#title           :dynamic_fib.py
#description     :This is example of dynamic programming.
#author          :Tanaji Sutar
#date            :2020-Jan-29
#python_version  :2.7/3  
#problem:Given an Array of n elements, find k elements that sums to s.
#Input :A=[2,8,15,30,4]  s=12  k=2 OUTPUT :2 & 4 sums to 12
#Input :A=[2,8,15,30,4]  s=40  k=3 OUTPUT :2,8 & 30 sums to 12 
#============================================================================================

def f(n,k,s):
    #n should not be zero
    if n>0:
        #print('f:',n,k,s)
        #Exclude n
        if A[n]>s:
            res=f(n-1,k,s)
            return res
        
        #end
        elif (k-1==0 and s-A[n]==0):
            #save index n into memo as it is included
            memo[k]=n
            return 0
        
        #consider n
        elif (k-1 >0 and s-A[n] >0):
            #check if n can be included
            res=f(n-1,k-1,s-A[n])
            if res==0:
                #if n can be included
                memo[k]=n
                return res
            else:
                #if n can not be included
                res=f(n-1,k,s)
    
        #dont consider n
        else:
            res=f(n-1,k,s)
            return res

if __name__ == "__main__":

    A=['#',2,8,15,30,4]
    print('A :%r'%A)
    
    #--Test case 1 :expected result:[None,2,5]
    k=2
    s=12
    n=len(A)-1  #number of elemnts
    memo=[None]*(k+1)
    res=f(n,k,s)
    print('---Test 1--')
      
    print('for k:%r,s:%r  Ans:%r ' %(k,s,[A[i] for i in memo[1:]] ))

    #--Test case 2 :expected result:[None,2,5]
    k=3
    s=40
    n=len(A)-1  #number of elemnts
    memo=[None]*(k+1)
    res=f(n,k,s)
    print('---Test 2--')
    print('for k:%r,s:%r  Ans:%r ' %(k,s,[A[i] for i in memo[1:]] ))

    
