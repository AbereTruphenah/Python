#max function
# arr=[-2,-4,-6,-8]
largest=max(arr)
print(largest)


#for loop
# # Sample array
arr = [3, 5, 1, 8, 2]

# Initialize the largest element with the first element
largest_element = arr[0]

# Loop through the array
for num in arr:
    if num > largest_element:
        largest_element = num

print("The largest element is:", largest_element)



#sorting
# Sample array
arr = [3, 5, 1, 8, 2]

# Sort the array
sorted_arr = sorted(arr)

# Get the largest element
largest_element = sorted_arr[-1]

print("The largest element is:", largest_element)