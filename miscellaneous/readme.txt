

def int2bin(integer, digits):
    #
    #User defined fundtion to get binary representation of given integer
    ######################################################################
    if integer >= 0:
        return bin(integer)[2:].zfill(digits)
    else:
        return bin(2**digits + integer)[2:]
       
       
Ex.combination = int2bin(2,3)
Ex.combination = int2bin(2,3)
Ex.combination = int2bin(2,3)
