#=============================================================================================
#!/usr/bin/env python
#title           :longestComnSubseq.py
#description     :Longest Common Subsequence.
#author          :Tanaji Sutar
#date            :2020-Jan-30
#python_version  :2.7/3  
#problem:Given two sequences, find the length of longest subsequence present 
# in both of them. A subsequence is a sequence that appears in the same relative order, 
# but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, 
# etc are subsequences of “abcdefg”
#LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
#LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
#============================================================================================

def lcs_rec_only(s1,s2,n,m):
    """
    This is only using recursion and withot memoization.
    A Naive recursive Python implementation of LCS problem.
    """
    if n==0 or m==0:
        #Any of two string is empty
        #print('zero')
        return 0
    
    elif s1[n-1] == s2[m-1]:
        #if equal
        res=1+lcs_rec_only(s1,s2,n-1,m-1)
        #print(s1[n-1])
    else:
        #if not equal
        tmp1=lcs_rec_only(s1,s2,n-1,m)
        tmp2=lcs_rec_only(s1,s2,n,m-1)
        res=max(tmp1,tmp2)
    return res

def lcs_rec_with_memo(s1,s2,n,m,Memo):
    """
    This is using recursion and with memoization.
    """
    if n==0 or m==0:
        #Any of two string is empty
        #print('zero')
        return 0
    
    if Memo[n][m]!=None:
        return Memo[n][m] #<------Added Extra
    
    elif s1[n-1] == s2[m-1]:
        #if equal
        res=1+lcs_rec_only(s1,s2,n-1,m-1)
        #print(s1[n-1])
    else:
        #if not equal
        tmp1=lcs_rec_only(s1,s2,n-1,m)
        tmp2=lcs_rec_only(s1,s2,n,m-1)
        res=max(tmp1,tmp2)
    
    Memo[n][m]=res #<------Added Extra
    return res

if __name__ == "__main__":
    
    s1='BATD'
    s2='ABACD'
    n=len(s1)
    m=len(s2)
    #print('start',n,m)
    ans=lcs_rec_only(s1,s2,n,m)
    print(ans)
    

    s1='AGGTAB'
    s2='GXTXAYB'
    n=len(s1)
    m=len(s2)
    #print('start',n,m)
    t=max(n,m) +1 #as in python idex start with zero,add 1 extra
    Memo=[[None]*t]*t #<------Added Extra
    #print(Memo)
    ans=lcs_rec_with_memo(s1,s2,n,m,Memo)
    print(ans)
    #print(Memo)

    
