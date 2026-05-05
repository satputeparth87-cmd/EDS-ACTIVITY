# import numpy as np

# # Input array from the user
# array1 = np.array(list(map(int, input().split())))

# # Searching
# search_value = int(input("Value to search: "))
# count_value = int(input("Value to count: "))
# broadcast_value = int(input("Value to add: "))

# # Find indices where value matches in array1

# # Count occurrences in array1

# # Broadcasting addition

# # Sort the first array
import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# 1. Find indices where value matches in array1
search_indices = np.where(array1 == search_value)[0]  # np.where returns a tuple, we take the first element
print(search_indices)

# 2. Count occurrences in array1
count_occurrences = np.count_nonzero(array1 == count_value)
print(count_occurrences)

# 3. Broadcasting addition (Add broadcast_value to each element)
# # Sort the first array