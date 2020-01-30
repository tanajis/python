###########################################################################################
#You are given a number N. You have to find the number of operations required to reach N from 0. 
#You have 2 operations available:
#   1.Double the number
#   2.Add one to the number
#Input:Give a number
#Output:print the minimum number of operations required to reach N from 0.
#Testcase1:
#Input  : N = 8
#Output : 4
#0 + 1 = 1, 1 + 1 = 2, 2 * 2 = 4, 4 * 2 = 8
#Testcase2:
#Input  : N = 7
#Output : 5
#0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 3 * 2 = 6, 6 + 1 = 7
###########################################################################################

#=============================================================================================
#!/usr/bin/env python
#title           :bst.py
#description     :Geeksforgeeks Que
#author          :Tanaji Sutar
#date            :2020-Jan-30
#python_version  :2.7/3
#============================================================================================

def findOprCnt(n,opcnt):
    if n==2:
        opcnt=opcnt+2
        return opcnt
    if n==1:
        opcnt=opcnt+1
        return opcnt
    else:
        if n%2!=0:
            #n is odd
            n=n-1
            opcnt=opcnt+1
            return findOprCnt(n,opcnt)
        else:
            #n is even
            n=n/2
            opcnt=opcnt+1
            return findOprCnt(n,opcnt)

if __name__ == "__main__":
    a=findOprCnt(8,0)
    print(a)
    a=findOprCnt(7,0)
    print(a)
    a=findOprCnt(10,0)
    print(a)
