# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# =====================================

# from collections import Counter

# nums = [1,1,1,2,2,3]
# n = 2

# cnt = Counter(nums)
# print(cnt)

# # Corrected list comprehension
# out = [k for k, v in cnt.items() if v >= n]
# print(out)







# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# nums = [1,1,1,2,2,3]
# k = 2
# d= {}
# for k in set(nums):
#     d[k]=nums.count(k)

# sorted_dict = sorted(d.items(), key= lambda x:x[1])
# print([i[0] for i in sorted_dict[:2]])



# nums = [1,1,1,2,2,3]
# k = 2

# nums_count = []
# for k in set(nums):
#     nums_count.append((k , nums.count(k)))

# sorted_nums = sorted(nums_count, key= lambda x:x[1])

# print(sorted_nums[:k])

