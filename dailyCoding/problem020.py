# This problem was asked by Google.
# Given two singly linked lists that intersect at some point, 
# find the intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
#  return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and 
# constant space.

#=============================================================================================
#!/usr/bin/env python
#title           :problem20.py
#description     :DailyCoding #20
#author          :Tanaji Sutar
#date            :2020-feb-18
#python_version  :2.7/3
#ref             :
#============================================================================================


#Approach 1
#concat both, sort and find element whith curr==prev
#Complexity is O(m+n) if complexity of sorted function is considered as 1

def Approach1(A,B):
    C=A+B
    C=sorted(C)
    prev=None
    for i in range(len(C)):
        
        if i==0:
            prev=C[i]
            continue
        else:
            curr=C[i]
            if curr==prev:
                #print(curr)
                return curr
        #print('curr',curr,'prev',prev)
        prev=curr


def Approach2(A,B):
    #Approach2
    #using Hash map

    dict={}
    #if visited, 1 else 0

    for i in A:              # -----n times
        dict[i]=1

    #print(dict)
    for j in B:              #------m times

        try:
            if dict[j]==1:
                return j
                #print('value:',j)
        except Exception as e:
            #print('Key not present')
            dict[j]=1




        
if __name__ == "__main__":
    A=[3,4,8,10]
    B=[99,1,8,10]
    print(Approach1(A,B))
    print(Approach2(A,B))
