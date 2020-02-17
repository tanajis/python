#=============================================================================================
#!/usr/bin/env python
#title           :Knapsack_greedy.py
#description     :Knapsack .Greedy Approach
#author          :Tanaji Sutar
#date            :2020-Feb-17
#python_version  :2.7/3  
#============================================================================================

#ref :https://www.geeksforgeeks.org/fractional-knapsack-problem/
#Also called Fractional Knapsac

#Note :In the 0-1 Knapsack problem, we are not allowed to break items. 
# We either take the whole item or don’t take it.
# But Here In Fractional Knapsack, we can break items for maximizing the total value of knapsack.

def knapsack_greedy(wt,val,capacity):


    #calculate  profit per kg for all the products.
    #Also Keep index i so as to map to v and w later
    pByw=[[i,float(val[i]/wt[i])] for i in range(len(wt))]

    #sort profit per kg in decreasing order
    pByw=sorted(pByw, reverse=True,key = lambda x: x[1])
    print('Probit_per_kg Array sorted in desc:',pByw)

    #set c and profit to zero
    c=capacity
    max_profit=0

    for i in range(len(pByw)):
        #print('c',c)
        if c<=0:
            break
        #get max p/w
        maxm=pByw[i][1]
        ind=pByw[i][0]
        if (c-wt[ind])>=0:
            c=c-wt[ind]
            max_profit=max_profit+val[ind]
            print('Add value %r with weight %r' %(val[ind],wt[ind]))
        else:
            part=c/wt[ind]
            c=c-(wt[ind] *part)
            max_profit=max_profit+(val[ind] *part)
            print('Add %r of  value %r and weight %r' %(part,val[ind],wt[ind]))


    return int(max_profit)





if __name__ == "__main__": 
    wt = [10, 40, 20, 30] 
    val = [60, 40, 100, 120] 
    capacity = 50

    print('Input WT:%r ',wt)
    print('Input VAL:%r ',val)
    print('Maximum profit using Greedy approach is %r' %knapsack_greedy(wt,val,capacity))

    #Output Maximum value in Knapsack = 240
