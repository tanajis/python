def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Recursive call if item is a list
        else:
            flat_list.append(item)
    return flat_list

# Example usage:
nested = [1, [2, [3, 4], 5], 6, [7, 8]]
print(flatten(nested))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
 