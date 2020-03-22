#
# Position of rightmost set bit or Find first set bit
# Write a one line function to return position of first 1 from right to left, 
# in binary representation of an Integer
# Input :  18 (Binary Representation 010010)
# Output : 2
# Input  : 19 (Binary Representation 010011)
# Output : 1
#
def decToBinary(n):
    res = ''
    while(n>=1):
        res = str(n%2) + res  
        n = n/2

    return int(res)

def getrightMostSetBit(n):

    binary = decToBinary(n)
    binary = str(binary)
    i = len(binary) - 1
    flag = 0
    pos = 0
    #print(binary)
    while(i>=0):
        pos = pos + 1
        if binary[i] == '1':
            flag = 1
            break
        i = i - 1
    
    if flag == 1:
        return pos
    else:
        return None
    

if __name__ == "__main__":


    assert(getrightMostSetBit(18)) == 2
    assert(getrightMostSetBit(19)) == 1
    


