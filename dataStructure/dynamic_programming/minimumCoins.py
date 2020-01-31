# Ref : https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins/0
# Given a value N, total sum you have. You have to make change for Rs. N, and there is
#  infinite supply of each of the denominations in Indian currency, 
# i.e., you have infinite supply of { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000} 
# valued coins/notes, Find the minimum number of coins and/or notes needed to make 
# the change for Rs N.
# Input:
# The first line of input contains an integer T denoting the number of test cases. 
# Each test case consist of an Integer value N denoting the amount to get change for.
# Output:
# Print all the denominations needed to make the change in a separate line.
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 106
# Example:
# Input:
# 1
# 43
# Output:
# 20 20 2 1
# Explanation:
# Testcase 1: Sum of Rs 43 can be changed with minimum of 4 coins/ notes 20, 20, 2, 1.

#=============================================================================================
#!/usr/bin/env python
#title           :minimumCoins.py
#description     :Geeksforgeeks Que
#author          :Tanaji Sutar
#date            :2020-Jan-30
#python_version  :2.7/3
#ref             :https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins/0
#============================================================================================


#Dynamoic Approach is not working. Need to do further.

def moneyChange2(D,s,cnt):
    n=len(D)-1
    while(n>0):
        #print(n,D[n])

        if int(D[n])>s:
            #print('Exclude ',D[n])
            n=n-1
            continue
        
        elif int(D[n])==s:
            cnt=cnt+1
            s=s-D[n] #which is zero
            #print('include',D[n])
            
        else:
            k=int(s/int(D[n]))
            s=s-(int(D[n])*k)
            cnt=cnt+k
            #print('include',(str(D[n])+' ,')*k)
            continue
        n=n-1

    return cnt
"""
#Dynamoic approach not working
def moneyChange(n,s,cnt):
    print(n,D[n],s)
    if n<=0 or s<=0:
        cnt=cnt+0
        return cnt

    elif int(D[n])>s and n>0:
        #exclude D[n]
        return moneyChange(n-1,s,cnt)
    
    elif int(D[n])==s:
        s=0
        cnt=cnt+1
        return cnt

    #Consider D[n]
    elif n > 0 and s>D[n]:
        s1=s
        n1=n
        cnt1=cnt

        #exclude n
        res2=moneyChange(n-1,s,cnt)
        print('res2',res2)
        #Consider D[n]
        k=int(s/D[n])
        reminder=int(s%D[n])
        for i in range(k):
            w.append(D[n])
            s=s-(k*D[n])
            cnt=cnt+1
        if reminder==0:
            res1= cnt
        else:
            res1= moneyChange(n1-1,s1,cnt)
        
        if res1==0 and res2==0:
            return 0
        elif res1==0 and res2>0:
            return res2
        elif res2==0 and res1>0:
            return res1
        else:
            return min(res1,res2)
        min(res1,res2)
"""

if __name__ == "__main__":

    #denominations
    D=['#',1,2,5,10,20,50,100,200,500,2000]
    n=len(D)-1
    w=[]
    #res=moneyChange(n,43,0)

    #print('final',res)
    print(moneyChange2(D,43,0))


    E=['#',1, 2, 5, 10]
    print(moneyChange2(E,48,0))
