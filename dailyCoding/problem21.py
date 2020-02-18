# his problem was asked by Snapchat.
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
# find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


#1.sort array with  starting time
#2.for l in lectures
# if curr.start<pre.end give new room for all prev

#=============================================================================================
#!/usr/bin/env python
#title           :problem21.py
#description     :DailyCoding #21
#author          :Tanaji Sutar
#date            :2020-feb-18
#python_version  :2.7/3
#ref             :
#============================================================================================

L=[(30, 75), (0, 50), (60, 150)]
A=[]
for i in L:
    A.append((i[0],'S'))
    A.append((i[1],'E'))

#Sort A
A=sorted(A,key=lambda x: x[0])
#print(A)

rmcnt=0
opncnt=0
for i in A:
    if rmcnt==0:
        rmcnt=1
    else:
        if i[1]=='S':
            #if start, allocate room
            if opncnt>0:
                #If open exist, allocate among existing only
                opncnt=opncnt-1
            else:
                 #If open not exist, allocate new
                rmcnt=rmcnt+1
        else:
            #If closed release 
            opncnt=opncnt+1

print('Number of room required:',rmcnt)
