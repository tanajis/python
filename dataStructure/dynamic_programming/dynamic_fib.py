#=============================================================================================
#!/usr/bin/env python
#title           :dynamic_fib.py
#description     :This is demo of dynamic programming with fibonacci series.
#author          :Tanaji Sutar
#date            :2020-Jan-28
#python_version  :2.7/3  
#Notes: Fibonacci Series: 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
#============================================================================================

def fib_rec(n):
    #This is using just recursion
    if n==1 or n==2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)


def fib_rec_memo(n,memo):
    #This is fibonacci series using recursion and memoization.
    #memo needs to be declared outside the function(global) and cant be inside the function. 
    if n==1 or n==2:
        return 1
    elif memo[n] is not None:
        return memo[n]
    else:
        res=fib_rec_memo(n-1,memo)+fib_rec_memo(n-2,memo)
        memo[n]=res
        return res

def fib_bottom_up(n):
    #memo can be declared inside function.
    #No recursion is used.
    memo2=[None]*(n+1)
    
    if n==1 or n==2:
        return 1
    else:
        memo2[1]=1
        memo2[2]=1
        i=3
        while(i<=n):
            memo2[i]=memo2[i-1] +memo2[i-2]
            i=i+1
        
        return memo2[n]

if __name__ == "__main__":
    
    n=10
    
    print('Using recursion only:',fib_rec(n))

    #In python index starts at 0 hence take n+1 and keep start blank & unused
    memo=[None]*(n+1)
    #print(memo)
    print('Using recustion with memoization:',fib_rec_memo(n, memo))
    #print(memo)

    print('Using bottomup with memoization:',fib_bottom_up(n))
