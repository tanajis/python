# This problem was asked by Amazon.
# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a single count 
# and character. 
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
# Implement run-length encoding and decoding. You can assume the string to be 
# encoded have no digits and consists solely of alphabetic characters. 
# You can assume the string to be decoded is valid.

#=============================================================================================
#!/usr/bin/env python
#title           :problem029.py
#level           :Easy
#description     :Run leangth Encoding Dailycoding
#author          :Tanaji Sutar
#date            :2020-Mar-18
#python_version  :2.7/3  
#============================================================================================



def RLEncode(input_str):
    """
    This function returns the ecoded string.
    """
    cnt = 0
    prev_char = ''
    outString =''
    for char in input_str:
        if prev_char != '' and char != prev_char:
            outString = outString + str(cnt) + prev_char
            cnt = 0

        cnt += 1
        prev_char = char

    outString = outString + str(cnt) + prev_char
    return outString

def RLDecode(input_str):
    """
    This function returns the decoded string.
    """
    outString = ''

    for pos in range(0,len(input_str)):

        if (pos%2) == 0:
            cnt  = int(input_str[pos])
            continue

        else:
            for _ in range(cnt):
                outString = outString + input_str[pos]
    
    return outString



if __name__ == "__main__":

    assert RLEncode('AAAABBBCCDAA') ==  '4A3B2C1D2A'
    assert RLDecode('4A3B2C1D2A')   ==  'AAAABBBCCDAA'
