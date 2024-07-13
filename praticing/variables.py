# Because python is a dynamically typed language, we can change the variable data type after being assigned.

user_name, full_name = "yaz", "Yazan Farrah"  # assigning multiple variables in one line

# temp = user_name
#
# user_name = full_name
#
# full_name = temp
#
# del full_name  # Deletes a variable from the memory
#
# print(type(user_name))  # Returns the type of the variable
#
# print(user_name)

complex_number = 4 + 1j

print(type(complex_number))

# Convert float to int, we can convert int to float as well

num = 12.9

print(int(num))

age = 24

age = str(age)

print(age, type(age))
