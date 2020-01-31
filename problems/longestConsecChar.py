#=============================================================================================
#!/usr/bin/env python
#title           :longestConsecChar.py
#description     :Longest Consecutive Character
#author          :Tanaji Sutar
#date            :2020-Jan-30
#python_version  :2.7/3
#ref             :
#input           :'AABCDDBBBEA'
#output          : B:3
#============================================================================================

def longestConsecChar(str):

    overall_max_cnt=0
    overall_max_c=None

    for i in range( len(str)):
        if i==0:
            #first character
            curr_cnt=1
            curr_c=str[i]
            overall_max_cnt=curr_cnt
            overall_max_c=curr_c
        else:
            prev_cnt=curr_cnt
            prev_c=curr_c
            curr_c=str[i]
            curr_cnt=1
            if curr_c==prev_c:
                #matches prev
                curr_cnt=curr_cnt+prev_cnt
                if curr_cnt > overall_max_cnt:
                    overall_max_cnt=curr_cnt
                    overall_max_c=curr_c

    return overall_max_c,overall_max_cnt

if __name__ == "__main__":
    
    str='AABCDDBBBEA'
    print('Ans:',longestConsecChar(str))
