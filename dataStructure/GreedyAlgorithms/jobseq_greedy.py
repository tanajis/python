#=============================================================================================
#!/usr/bin/env python
#title           :jobseq_greedy.py
#description     :Greedy Algorithms
#author          :Tanaji Sutar
#date            :2020-Feb-19
#python_version  :2.7/3
#ref             :
#============================================================================================

def jobseq(A,B,t):
    #enumerates to give index
    A=enumerate(A,start=0)
    A2=[]
    for ind,prof in A:
        A2.append([ind,prof])

    #sort descending profit
    A2=sorted(A2,reverse=True,key=lambda x:x[1])
    #print(A2)

    timeslots=[None]*t
    #print(timeslots)
    for i in A2:
        #get index 
        ind=i[0]
        #get deadline
        d=B[ind]
        #print(ind,d)
        #as deadline start from 1 but timeslot index start from 0 henec reduce deadline by 1
        #so as to match with slot index
        d=d-1

        #check if slot available.Check from last
        j=t-1
        while(j>=0):
            #print('slot',j,d)
            if timeslots[j] is None and j<=d:
                timeslots[j]=i
                #print('fits',j,d)
                break
            j=j-1

    return timeslots
    #print(timeslots)

if __name__ == "__main__":

    print('test2')
    A=[100,19,27,25,15]
    B=[2,1,2,1,3]
    t=3

    print(jobseq(A,B,3))

    print('test2')
    A=[20,15,10,5,1]
    B=[2,2,1,3,3]
    t=3

    print(jobseq(A,B,3))
    print('Note :Jobs numbering starts from Zero')
