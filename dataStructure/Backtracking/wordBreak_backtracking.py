#############################################################################################################
#IMP Note : 
# only finds whether it is possible to break a word or not  --->Dynamic Programing
# print all possible word breaks                            --->Backtracking  Programing
#
##############################################################################################################
# Ref : https://www.geeksforgeeks.org/word-break-problem-using-backtracking/
# Given a valid sentence without any spaces between the words and a dictionary of valid English words, 
# find all possible ways to break the sentence in individual dictionary words.
#
# Consider the following dictionary 
# { i, like, sam, sung, samsung, mobile, ice, 
#   cream, icecream, man, go, mango}
#
# Input: "ilikesamsungmobile"
# Output: i like sam sung mobile
#         i like samsung mobile
#
# Input: "ilikeicecreamandmango"
# Output: i like ice cream and man go
#         i like ice cream and mango
#         i like icecream and man go
#         i like icecream and mango
###############################################################################




#
# Step 1: start scanning the sentence from left.
# Step 2:If we find a valid word, check whether rest of the sentence can make valid words or not.(Recursively)
# Step 3:If remaining portion is not further separable -->Cancle this word and keep on searching for the next word
# Step 4:If remaining portion is further separable     --> select this word
# step 5: continue to search next word 

from copy import deepcopy

def existInDict(w,dict:list):
    if dict.__contains__(w):
        return True
    else:
        return False

def wordBreak_backtracking(s,start,dict,stk):

    #stknew = deepcopy(stk)
    #print('call',s,start,stk)
    l = len(s)

    if start == l:
        return True
    w=''
    #print('lll',l)

    for i in range(start,l):
        #print('i' ,i)
        w = w + s[i]
        #print('w',w)
        if existInDict(w,dict):
            #print('exist')
            #Add at the end of stack :stack push operation
            stk.append(w)
            #Word exist in dict, Check remaining portion is seperable
            res1 = wordBreak_backtracking(s,i+1,dict,stk)
            #If True then continue to next else pop/remove that word
            if res1 == True:
                #w = ''
                #IF we reached at the end of string then only print result
                if i == l-1:
                    print(stk)
                    #IMPORTANT
                    #at res1 above, it will automatically print the final result cosnidering word 'sam'
                    #Now remove that word 'sam' so that we can consider 'samsung'
                    #Result with word 'samsung' should not contain word 'sam' hence  pop it from stk
                    stk.pop()
                continue
            else:
                #Remove last elememt -stack pop
                stk.pop()

            

if __name__ == "__main__":


    dict = [ 'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango','and']
    str = "ilikesamsungmobile"

    #In python list can work as stack, queue etc
    stk =[]
    output=[]
    ans = wordBreak_backtracking(str,0,dict,stk)

    #print('hiiiii',output)

    print('test Case 2')

    dict = [ 'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango','and']
    str = "ilikeicecreamandmango"

    #In python list can work as stack, queue etc
    stk =[]
    output=[]
    ans = wordBreak_backtracking(str,0,dict,stk)
