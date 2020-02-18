# This problem was asked by Twitter.
# You run an e-commerce website and want to record the last N order ids in a log. 
# Implement a data structure to accomplish this, with the following API:
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log.
# i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


#=============================================================================================
#!/usr/bin/env python
#title           :problem16.py
#description     :Daily Coding problem#16
#author          :Tanaji Sutar
#date            :2020-Feb-18
#python_version  :2.7/3  
#============================================================================================

#This is Queue implementation  problem
#Array implementation 

def record(order_id,f,r,Que):
    if len(Que)==0:
        f=f+1
        r=r+1
        Que[f]=order_id
    else:
        #shift all element to next position to make Que[0] empty
        i=n-1
        while(i>0):
            Que[i]=Que[i-1]
            i=i-1
        
        Que[0]=order_id

        
def get_last(pos):
    return Que[pos]

if __name__ == "__main__":
    n=5
    Que=[None]*n
    f=-1
    r=-1

    print(Que)

    record(501,f,r,Que)
    print(Que)
    record(502,f,r,Que)
    print(Que)
    record(503,f,r,Que)
    print(Que)
    record(504,f,r,Que)
    print(Que)
    record(505,f,r,Que)
    print(Que)
    record(506,f,r,Que)

    print(get_last(1))



