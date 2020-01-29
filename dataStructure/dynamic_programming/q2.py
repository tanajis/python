#A=[2,8,15,30,4]  s=12  k=3
#find k emenets whose sum rquals to 2
#Ex. 2+4=12  --only 2 elemts



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
    print('for k:%r,s:%r  Ans:%r ' %(k,s,memo[1:]))

    #--Test case 2 :expected result:[None,2,5]
    k=3
    s=40
    n=len(A)-1  #number of elemnts
    memo=[None]*(k+1)
    res=f(n,k,s)
    print('---Test 2--')
    print('for k:%r,s:%r  Ans:%r ' %(k,s,memo[1:]))

    

