# Sample array
arr = [1]

# Remove duplicates and sort the array
unique_sorted_arr = sorted(set(arr))

# Get the second smallest and second largest elements
if len(unique_sorted_arr) > 1:
    second_smallest = unique_sorted_arr[1]
    second_largest = unique_sorted_arr[-2]  # Second last element
else:
    second_smallest = None
    second_largest = None

print("The second smallest element is:", second_smallest)
print("The second largest element is:", second_largest)
