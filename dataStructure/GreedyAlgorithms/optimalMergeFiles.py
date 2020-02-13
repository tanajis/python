#=============================================================================================
#!/usr/bin/env python
#title           :optimalMergeFiles.py
#description     :Greedy Approach :Optimal Merge pattern
#author          :Tanaji Sutar
#date            :2020-Feb-13
#python_version  :2.7/3  
#Notes           : Given a list of size of each file, provide optimal way of merging.
#============================================================================================


def optimalMergeFiles(f):
    print('Input :',f)
    #sort in the increasing order
    f2=sorted(f)
    #print(f2)

    #if number of files is n then we need to merge n-1 times
    remaining=f2
    for i in range(1,len(f)):
        #print(remaining)
        #get minimum
        m1=min(remaining)
        remaining.remove(m1)
        m2=min(remaining)
        remaining.remove(m2)
        print('Merging %r and %r' %(m1,m2))
        remaining.append(m1+m2)
    
    print('final size %r' %(remaining[0]))
if __name__ == "__main__":
    f=[20,30,10,5,30]
    res1=optimalMergeFiles(f)
    
    f=[6,5,2,3]
    res1=optimalMergeFiles(f)
