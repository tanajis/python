# https://leetcode.com/problems/merge-two-sorted-lists/description/

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4,4]
# Output: [1,1,2,3,4,4,4]


l1= [1,2,4]
l2 = [1,3,4,4]

i = 0
j = 0
out=[]
while(i < len(l1) and j < len(l2)):
    # Until the smallest list finishes
    if l1[i] <= l2[j]:
        out.append(l1[i])
        i = i+1
    else:
        out.append(l2[j])
        j = j + 1

# Now append remaining elemnets from the larger list.
    out = out + l1[i:]

if j < len(l2):
    out = out + l2[j:]

print(out)