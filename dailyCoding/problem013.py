# This problem was asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


#=============================================================================================
#!/usr/bin/env python
#title           :problem013.py
#level           :HARD
#description     :Maximum Substring with k elements #DailyCoding 013 
#author          :Tanaji Sutar
#date            :2020-Mar-01
#python_version  :2.7/3  
#Note              :This is an example of DP.I have solved with total papaerwork and spending 2.30 hrs
#============================================================================================

#Note : longest   -->DP problem

#Algorithm (By tanaji sutar)
# f(s,n,max,maxlen,distinctChars):
# Base case : all char processed(n==0) return cnt
# Check if s[n] present in  distinctChars?
# If present we can consider s[n]. call f(s,n-1,s[n]+max, maxlen+1,distinctChars)
# If not present Check if can we add directly len(distinctChars) < k ?
#If Yes then consider s[n] :
#   s[n] to distinctChars Array.
#   increase maxlen by 1
#   add s[n] to max
#   call f(s,n-1,max,maxlen,distinctChars)
#If No then:
#  if we want to include s[n]
#           trim the max string from first occurance of first element in distinctChars
#           remove first element added to distinctChars
#           add s[n] to end of distinctChars
#           add s[n] to max string
#           increase maxlen by 1
#           call f(s,n-1,max,maxlen,distinctChars)
#
# if we want to exclude s[n]
#       make distinctChars empty
#       set max = ''
#       set maxlen = 0
#       call f(s,n-1,max,maxlen,distinctChars)


def longestSubstringKDistinctChars(s,k,n,maxString,maxlen,distinctChars):

    #print('call',n,maxString,maxlen,distinctChars)
    # Base case : all char processed return cnt
    if n < 0:
        return maxlen,maxString,distinctChars
    else:
        if  distinctChars.count(s[n])  == 1:
            #print('here0')
            #char already present in distinctChars, no need to add and can cosider it
            maxString = s[n] + maxString
            maxlen += 1
            if n == 1:
                #If s[n] is last character return the values directly
                return maxlen,maxString,distinctChars
            else:
                return longestSubstringKDistinctChars(s,k,n-1,maxString, maxlen,distinctChars)

        else:
            #If not present 
            maxlen1 = 0
            maxlen2 = 0
            maxlen3 = 0
            #Check if we can add it directly?
            if len(distinctChars) < k :
                #print('here1')
                temp_distinctChars = [i for i in distinctChars]
                temp_distinctChars.append(s[n])
                maxlen1,maxString1,distinctChars1 = longestSubstringKDistinctChars(s,k,n-1,str(s[n]) + maxString, maxlen + 1,temp_distinctChars)

            if len(distinctChars) == k :
                #we need to remove 1 existing char from distinctChars
                #exchar is character to be excluded
                exchar = distinctChars[0]
                temp_distinctChars = [i for i in distinctChars]
                temp_distinctChars.pop(0)
                
                #Now We have room so insert s[n] in distinctChars
                temp_distinctChars.append(s[n])

                #get the index where first occurance of exchar present
                index = maxString.find(str(exchar), 0)
                #trim string.Remove part from first occurance of exchar
                temp_maxString = str(maxString[0:index])

                #add s[n] to maxString
                temp_maxString = str(s[n] + temp_maxString)

                #update maxlen 
                temp_maxlen = len(temp_maxString)

                #print('here2.1')
                maxlen2,maxString2,distinctChars2 = longestSubstringKDistinctChars(s,k,n-1,temp_maxString, temp_maxlen,temp_distinctChars)
                #print('here3')
                #or we can simple exclude

                maxlen3,maxString3,distinctChars3 = longestSubstringKDistinctChars(s,k,n-1,maxString, maxlen,distinctChars)
                #print('here4')

            if maxlen1 >= maxlen2 and maxlen1 >= maxlen3:
                return maxlen1,maxString1,distinctChars1
            elif maxlen2 >= maxlen1 and maxlen2 >= maxlen3:
                return maxlen2,maxString2,distinctChars2
            elif maxlen3 >= maxlen2 and maxlen3 >= maxlen1:
                return maxlen2,maxString2,distinctChars2


if __name__ == "__main__":
    s = 'abcba'
    k = 2
    n=len(s) - 1 #index starts from 0
    maxString = ''
    maxlen = 0 
    distinctChars =[]
    print('ans:',longestSubstringKDistinctChars(s,k,n,maxString,maxlen,distinctChars))

