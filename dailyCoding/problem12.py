##################################################################################
# Problem 12
# This problem was asked by Amazon.
# There exists a staircase with N steps, and you can climb up either
# 1 or 2 steps at a time. Given N, write a function that returns the number 
# of unique ways you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
#################################################################################

#=============================================================================================
#!/usr/bin/env python
#title           :problem12.py
#description     :DailyCoding #12
#author          :Tanaji Sutar
#date            :2020-feb-11
#python_version  :2.7/3
#ref             :https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
#Note            : This is an example of fibbonancy puzzles .
#Find more at http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibpuzzles.html
#============================================================================================
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-1)+fib(n-2)

if __name__ == "__main__":
    n=4
    ans=fib(n)
    print(ans)
