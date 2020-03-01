
# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, 
# substitute the “e” for “i”, and append a “g”.
# Given two strings, compute the edit distance between them.
#=============================================================================================
#!/usr/bin/env python
#title           :problem031.py
#description     :Minimum Edit Distance between two string #DailyCoding
#author          :Tanaji Sutar
#date            :2020-Mar-01
#python_version  :2.7/3  
#============================================================================================


def minimumEditDist(s1,s2,m,n):
    if m == 0:
        return n
    
    if n == 0:
        return m
    
    #if mathcing
    if s1[m-1] == s2[n-1]:
        return(minimumEditDist(s1,s2,m-1,n-1))


    return 1 + min(
        minimumEditDist(s1,s2,m,n-1)      #if s2[n] not found in s1 so insert into s1
        ,minimumEditDist(s1,s2,m-1,n)     #if s1[m] is not found in s2(unrequired), delete it from s1
        ,minimumEditDist(s1,s2,m-1,n-1)     #if replace s1[n] by s2[m].Both m&n need to be reduced
    )


str1 = "sunday"
str2 = "saturday"
print(minimumEditDist(str1, str2, len(str1), len(str2)) )

str1 = "kitten"
str2 = "sitting"
print(minimumEditDist(str1, str2, len(str1), len(str2)) )

