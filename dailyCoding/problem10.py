# Good morning! Here's your coding interview problem for today.
# This problem was asked by Apple.
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

#=============================================================================================
#!/usr/bin/env python
#title           :problem10.py
#description     :Daily coding
#author          :Tanaji Sutar
#date            :2020-Feb-11
#python_version  :2.7/3
#ref             :
#============================================================================================


import datetime
import time

def schedule(f,n):
    #as n is in millisecond, we need to convert it in sec as per required by python sleep method.
    time.sleep(n/1000)
    print(datetime.datetime.now())
    res =f()
    
def f1():
    print('inside function f1')


if __name__ == "__main__":
    print(datetime.datetime.now())
    #As per que, we need pass interval in millisec 1 sec =1000 milli sec
    schedule(f1,3000)
    
