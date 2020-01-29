#=============================================================================================
#!/usr/bin/env python
#title           :kadane_max_subarray.py
#description     :Largest Sum Contiguous Subarray. Kadane's Algorithm
#author          :Tanaji Sutar
#date            :2020-Jan-29
#python_version  :2.7/3  
#problem:find the sum of contiguous subarray within a one-dimensional array 
# of numbers which has the largest sum.
#Input :A=[-2,3,2,-1]  OUTPUT : 5 (3 and 2 are contineous and sum is maximum)
#============================================================================================


def kadane_max_subarray(A):
    global_max_sum=None
    for i in range(len(A)):
        if i==0:
            #intialize sums equals to first element of given Array.
            current_max_sum=A[i]
            global_max_sum=A[i]
        else:
            current_max_sum=max(A[i],(current_max_sum+A[i]))
            if current_max_sum>global_max_sum:
                global_max_sum=current_max_sum
    
    return global_max_sum

if __name__ == "__main__":

    A=[-2,-3,4,-1,-2,1,5,-3]
    print(kadane_max_subarray(A))

    B = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
    print(kadane_max_subarray(B))
    
    C = [-2,3,2,-1] 
    print(kadane_max_subarray(C))

    D=[-2,1-3,4,-1,2,1,-5,4]
    print(kadane_max_subarray(D))



