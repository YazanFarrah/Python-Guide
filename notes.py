# using reverse in sorted reverses the array elements

arr = [1, 2, 4, 5, 6]
arr.sort(reverse=True)
# or
sorted(arr, reverse=True)

# If we want to apply custom condition for sorting, we use the key, and usually the key takes a function

arr2 = ["0", "00000", "0000", "00", "000"]

print(sorted(arr2, key=len))

# For example here we are sorting the array based on the length, starting from the shortest to longest


# When comparing to None, use "is" better

none_val = None

print(none_val is None)  # True
print(none_val == None)  # True
