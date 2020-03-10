#=============================================================================================
#!/usr/bin/env python
#title           :problem027.py
#description     :DailyCoding #027   EASY : Stack applications
#author          :Tanaji Sutar
#date            :2020-Mar-10
#python_version  :2.7/3
#============================================================================================

# This problem was asked by Facebook.
# Given a string of round, curly, and square open and closing brackets, 
# return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

# This is use case of STACK data structure
#-----ALgorithm-------
# Declare a character stack S.
# Now traverse the expression string exp.
# If the current character is a starting bracket (‘(‘ or ‘{‘ or ‘[‘) then push it to stack.
# If the current character is a closing bracket (‘)’ or ‘}’ or ‘]’) 
# then pop from stack and if the popped character is the matching starting bracket then fine else parenthesis are not balanced.
# After complete traversal, if there is some starting bracket left in stack then “not balanced”


def validateString(s):

    if len(s) == 1:
        return False
    
    if s[0] == ')' or s[0] == '}' or s[0] == ']' or s[-1] == '[' or s[-1] == '(' or  s[-1] == '{':
        return False
    
    else:

        stk =[]
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stk.append(c)
            elif c == ')'  or c == ']' or c == '}' :
                if  c == ')' and stk[-1] =='(':
                    stk.pop()
                elif  c == '}' and stk[-1] =='{':
                    stk.pop()
                elif  c == ']' and stk[-1] =='[':
                    stk.pop()
                else :
                    return False
        if stk:
            #if stack is not empty then string is not balanced, return false
            return False
        else:
            #if stack is  empty then string is  balanced, return True
            return True

if __name__ == "__main__":
    
    s = '([])[]({})'
    print(s, validateString(s))

    s = '([)]'
    print(s, validateString(s))

    s = '((()'
    print(s, validateString(s))

    # For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.



              
