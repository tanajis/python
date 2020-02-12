

#=============================================================================================
#!/usr/bin/env python
#title           :toh_recursive.py
#description     :Tower Of Honoi
#author          :Tanaji Sutar
#date            :2020-feb-12
#python_version  :2.7/3
#ref             :
#Note            :Disk count start from top.if n=4, dist at the top is 4rth and disk at bottom is 1
#============================================================================================



def toh(n,from_towr,to_towr,med_towr):
    if n==1:
        print('Move disk 1 from tower %s to % s' %(from_towr,to_towr))
        return
    
    toh(n-1,from_towr,med_towr,to_towr)
    print('Move disk %r from tower %s to % s' %(n,from_towr,to_towr))
    toh(n-1,med_towr,to_towr,from_towr)
    return None

if __name__ == "__main__":
    n=4
    toh(4,'A','C','B')
