# data_in =  ["h","e","l","l","o"]
# start = 0
# end = len(data_in)-1
# while(start<end):
#     data_in[start],data_in[end] = data_in[end],data_in[start]
#     start +=1
#     end -=1
# print(data_in)

# # ---------------------
# # # Another way
# # for i in range(len(a)//2):
# #     tmp = a[i]
# #     a[i] = a[-1-i]
# #     a[-1-i] = tmp


import math
data_in =  ["h","e","a","d","c","k"]
s =  0
e = len(data_in)-1
print(s,e)


while(s<e):
    data_in[s],data_in[e]=data_in[e],data_in[s]
    s = s+1
    e=e-1
print(data_in)
