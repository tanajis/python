#=============================================================================================
#!/usr/bin/env python
#title           :longestCommonString.py
#description     :#https://practice.geeksforgeeks.org/problems/longest-common-substring/0
#author          :Tanaji Sutar
#date            :2020-Feb-04
#python_version  :2.7/3  
#problem         :Given two strings X and Y. The task is to find the length of the longest common substring.
#Input : ABCDGH and ACDGHR
#Output : 4 because  CDGH is longest
#Input :abcdxyz and xyzabcd output  : 4
#============================================================================================

#Note : Memoization can be used , but I didnt used here.

def longestCommonString(s1,s2,n,m,cnt):

    #print(s1,s2,n,m)
    if n==1 or m==1:
        #only one char remaining
        #print('compare L1:',s1[n-1],s2[m-1]) 
        if s1[n-1]==s2[m-1]:
            #print(s1[n-1])
            cnt=cnt+1
            #print('cnt',cnt)
            return cnt
        else:
            return cnt
    else:
        if s1[n-1]==s2[m-1]:
            #cnt=1+longestCommonString(s1[:n-1],s2[:m-1],n-1,m-1,cnt)
            cnt=cnt+1+longestCommonString(s1[:n-1],s2[:m-1],n-1,m-1,0)
            return cnt
        else:
            cnt1=cnt2=cnt
            res1=longestCommonString(s1[:n-1],s2[:m],n-1,m,0)
            res2=longestCommonString(s1[:n],s2[:m-1],n,m-1,0)
            #res1=longestCommonString(s1[:n-1],s2[:m],n-1,m,cnt1)
            #res2=longestCommonString(s1[:n],s2[:m-1],n,m-1,cnt2)
            cnt=cnt+max(res1,res2)
        #print('cnt',cnt)
        return cnt 

if __name__ == "__main__":

    #Test case #1
    s1='ABCDGH'
    s2='ACDGHR'
    n=len(s1)
    m=len(s2)
    cnt=0
    print('Ans:',longestCommonString(s1,s2,m,n,cnt))
    #print(s1[:n],s1[:n+1])

    #Test case #2
    s1='GeeksforGeeks'
    s2='GeeksQuiz'
    n=len(s1)
    m=len(s2)
    cnt=0
    #print(s1[n-1],s2[m-1])
    print('Ans:',longestCommonString(s1,s2,n,m,cnt))

    #Test case #3
    s1='zxabcdezy'
    s2='yzabcdezx'
    n=len(s1)
    m=len(s2)
    cnt=0
    #print(s1[n-1],s2[m-1])
    print('Ans:',longestCommonString(s1,s2,n,m,cnt))


    #Test case #4
    s1='abcdxyz'
    s2='xyzabcd'
    n=len(s1)
    m=len(s2)
    cnt=0
    #print(s1[n-1],s2[m-1])
    print('Ans:',longestCommonString(s1,s2,n,m,cnt))

