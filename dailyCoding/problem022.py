# This problem was asked by Microsoft.
# Given a dictionary of words and a string made up of those words (no spaces), 
# return the original sentence in a list. If there is more than one possible 
# reconstruction, return any of them. 
# If there is no possible reconstruction, then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and 
# the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and 
# the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] 
# or ['bedbath', 'and', 'beyond'].

#=============================================================================================
#!/usr/bin/env python
#title           :problem022.py
#description     :DailyCoding #22 #Medium
#author          :Tanaji Sutar
#date            :2020-mar-03
#python_version  :2.7/3
#ref             :
#============================================================================================

import copy

def findWords(A,s):

    res =[]
    temp = copy.deepcopy(A)
    tempstr = ''
    k = 0
    for c in s :
        tempstr =tempstr + c
        #print(c,tempstr)
        temp = [wrds if tempstr ==  str(wrds[:k+1]) else '' for wrds in temp]
        while temp and temp.__contains__(''):
            temp.remove('')
        #print('temp:',temp)
        for w2 in temp:
            if w2 == tempstr:
                if len(temp) == 1:

                    res.append(w2)
                    temp = copy.deepcopy(A)
                    temp.remove(w2)
                    tempstr = ''
                    k = -1

        k = k + 1
    return res

if __name__ == "__main__":
    A = ['quick', 'brown', 'the', 'fox']
    s = "thequickbrownfox"
    ans = findWords(A,s)
    
    print(ans)

    print('Test case 2')
    A= ['bed', 'bath', 'bedbath', 'and', 'beyond']
    s =  "bedbathandbeyond"

    ans = findWords(A,s)
    print(ans)
