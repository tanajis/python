def find_missing_number(nums, n):
    # Calculate the expected sum of numbers from 1 to n
    total_sum = n * (n + 1) // 2
    # Subtract the sum of given numbers to find the missing number
    return total_sum - sum(nums)

# Example usage
nums = [1, 2, 4, 5, 6]  # Missing 3
n = 6
print(find_missing_number(nums, n))  # Output: 3