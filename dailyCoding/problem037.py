
# This problem was asked by Google.
# The power set of a set is the set of all its subsets. Write a function that,
# given a set, generates its power set.
# For example, given the set {1, 2, 3}, 
# it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

#=============================================================================================
#!/usr/bin/env python
#title           :problem037.py
#description     :Given a set, return power set of it.
#author          :Tanaji Sutar
#date            :2020-Mar-20
#python_version  :2.7/3
#============================================================================================


#ref :https://www.geeksforgeeks.org/power-set/
#Power Set Power set P(S) of a set S is the set of all subsets of S. 
# For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
# If there are n elements then we can have 2^n possible subsets in powerset

#Get how many distinct elements
# Here 3 (1,2,3) or a,b,c
#we can have maximum  2^3 = 8 possible combinations
#map the numbres to positions
# p1,p2,p3
# |  |  |
# 0  0  0   <--- put amoung 0 and 1 to try combination
#
# If 0, dont take that element in subset
# If 1, dont take that element in subset

""""
Example 2
Set  = [a,b,c]
power_set_size = pow(2, 3) = 8
Run for binary counter = 000 to 111

Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    010                    -> b
    011                    -> ab
    100                    -> c
    101                    -> ac
    110                    -> bc
    111                    -> abc
"""
def int2bin(integer, digits):
    #
    #User defined fundtion to get binary representation of given integer
    ######################################################################
    if integer >= 0:
        return bin(integer)[2:].zfill(digits)
    else:
        return bin(2**digits + integer)[2:]

def getPowerSet(inputSet):
    element_count = len(inputSet)
    tot_possible_subsets = pow(2,element_count)


    powerSet = []
    for i in range(tot_possible_subsets):        
        combination = int2bin(i,element_count)

        #if 1 -->include and if 0 -->exclude
        # position of digit ==position of element in  inputSet
        #print(combination)
        subset = []
        for pos in range(element_count):
            if combination[pos] == '1':
                subset.append(inputSet[pos])

        powerSet.append(subset)
    
    return powerSet



if __name__ == "__main__":
    
    print('Powerset of [1,2,3] : %r' % getPowerSet([1,2,3]))
    print("Powerset of ['a','b','c'] : %r " % getPowerSet(['a','b','c']))

    assert getPowerSet([1,2,3]) == [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
    assert getPowerSet(['a','b','c']) == [[], ['c'], ['b'], ['b', 'c'], ['a'], ['a', 'c'], ['a', 'b'], ['a', 'b', 'c']]
