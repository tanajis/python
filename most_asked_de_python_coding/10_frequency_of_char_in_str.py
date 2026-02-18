





def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example usage
input_str = "python programming"
freq = char_frequency(input_str)
print(freq)


# ================================

# suing collections

from collections import Counter

def char_frequency(s):
    return dict(Counter(s))

# Example usage
input_str = "python programming"
freq = char_frequency(input_str)
print(freq)