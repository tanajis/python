# Word count in a list of strings 
# https://leetcode.com/problems/most-common-word/

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Note that words can not contain punctuation symbols. 

# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:

# Input: paragraph = "a.", banned = []
# Output: "a"
 

# Constraints:

# 1 <= paragraph.length <= 1000
# paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
# 0 <= banned.length <= 100
# 1 <= banned[i].length <= 10
# banned[i] consists of only lowercase English letters.


import re
from collections import Counter

def most_common_word(paragraph, banned):
    # Normalize paragraph by removing punctuation and lowering case
    words = re.findall(r'\w+', paragraph.lower())
    
    banned_set = set(banned)
    
    # Count words excluding banned ones
    counts = Counter(word for word in words if word not in banned_set)
    
    # Return the word with the highest frequency
    return counts.most_common(1)[0][0]

# Example usage:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(most_common_word(paragraph, banned))  # Output: "ball"

################ witout cpllection@@#############


import re

def most_common_word_no_collections(paragraph, banned):
    words = re.findall(r'\w+', paragraph.lower())
    banned_set = set(banned)
    
    freq = {}
    for word in words:
        if word not in banned_set:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
    
    # Find the word with the maximum frequency
    max_count = 0
    result = ""
    for word, count in freq.items():
        if count > max_count:
            max_count = count
            result = word
    return result