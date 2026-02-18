# https://leetcode.com/problems/intersection-of-two-arrays/description/

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 


 def intersection(nums1, nums2):
    # Convert both lists to sets to get unique elements
    set1 = set(nums1)
    set2 = set(nums2)
    # Intersection of two sets
    result = set1 & set2
    # Convert to list before returning
    return list(result)

# Example usage:

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))  # Output: [2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))  # Output: [9, 4] or [4, 9]


# =============================Anotehr appprach:

def intersection_alternate(nums1, nums2):
    # Determine smaller and larger list
    if len(nums1) < len(nums2):
        small, large = nums1, nums2
    else:
        small, large = nums2, nums1

    result = []
    large_set = set(large)  # Convert larger list to set for O(1) lookup
    seen = set()            # To keep track of already added elements

    i = 0
    while i < len(small):
        elem = small[i]
        if elem in large_set and elem not in seen:
            result.append(elem)
            seen.add(elem)
        i += 1

    return result