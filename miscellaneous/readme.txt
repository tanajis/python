

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



#create Board 
    # Note if we use [0]*n  or [None]*n  then it makes shollow copies and when we update any one all get updated which is worng
    board = []
    for row in range(n):
        temp = []
        for col in range(n):
            temp.append(0)
        board.append(temp)

[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
