#=============================================================================================
#!/usr/bin/env python
#title           :knapsac_dyn.py
#description     :Dynamic Programing
#author          :Tanaji Sutar
#date            :2020-Jan-30
#python_version  :2.7/3
#ref             :https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
#============================================================================================


def knapSack(w,wt,val,n):
    #print(w,wt,val,n)
    #print(wt[n])
    if n==0 or w==0:
        return 0
    #Exclude
    if wt[n]>w:
        return knapSack(w,wt,val,n-1)
    
    #Consider
    #print('val',val)
    #Including n
    res1=val[n]+knapSack(w-wt[n],wt,val,n-1)
    #Excluding n
    res2=knapSack(w,wt,val,n-1)

    res=max(res1,res2)

    return res
if __name__ == "__main__":

    val = [60, 100, 120] 
    wt = [10, 20, 30] 
    w = 50
    n = len(val)-1
    print(knapSack(w , wt , val , n) )
