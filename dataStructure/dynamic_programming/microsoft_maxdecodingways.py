#=============================================================================================
#!/usr/bin/env python
#title           :microsoft_maxdecodingways.py
#description     :CS DOJO microsoft Que.Example of Dynamic programming using recursion.
#author          :Tanaji Sutar
#date            :2020-Jan-29
#python_version  :2.7/3  
#problem         :Count Possible Decodings of a given Digit Sequence
#Input:  digits[] = "121"
#Output: 3 As The possible decodings are "aba", "au", "la"
#Input :"12345" output : 3  as  3 ways : abcde,lcde,lude
#============================================================================================

#CS DOZO facebook que
#a=1,b=2,c=3.....z=26
#12345 -->12,3,4,5 or 1,2,3,4,5 or 1,23,4,5 -->3 ways



def decode(s,n):
    if n==0:
        #empty string  ""-->"" one way only
        return 1
    if s[0]=='0':
        #if string starts with 0 Ex. 011,0,0344. Cant decode as no mapping for 0
        #hence return zero ways 
        return 0

    #form number from first two of the char of string
    p=int(str(s[0:2]))
    #print('p:',p)
    if p>10 and p <=27:
        #remove first element & pass. remove 2 elemements and pass
        res=decode(s[1:],n-1) +decode(s[2:],n-2)
    else:
        #remove first char and pass
        res=decode(s[1:],n-1)

    return res

if __name__ == "__main__":
    
    #s="12345"
    s="123"
    n=len(s)
    #print(n)
    ans=decode(s,n)
    print('Number of ways:',ans)
