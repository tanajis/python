Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.



f(A,n):
  if memo[n]:
    return memo[n]
  
  #include n
  res1 = A[n] + f(A,n-1)
  #exclude n
  res2 = f(A,n-1)
  
  out=max(0,res1,res2)
  memo[n] = out
  return out

