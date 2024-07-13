# # While loops
#
# # while condition:
# #     statement
# #     statement
# #     statement
#
#
# count = 0
#
# while count <= 5:
#     print(f"Count is:{count}")
#     count += 1
#
# triangle_count = 0
#
# while triangle_count < 5:
#     print("*" * (triangle_count + 1))
#     triangle_count += 1
#
# name = "Yazan"
#
# name_count = 0
#
# while name_count < len(name):
#     print(name[name_count])
#     name_count += 1
#
# yaz = ["Yaz", "Yazan", "Yazou", "Begin"]
#
# list_count = 0
#
# while list_count < len(yaz):
#     print("Name:", yaz[list_count])
#     list_count += 1
#
# # Find if a value exist in a list
#
# i = 0
#
# while i < len(yaz):
#     print(f"#{i + 1} Still searching")
#     if yaz[i] == "Yazan":
#         print(f"Found it: {yaz[i]}")
#         break  # I did a break, so we don't need to iterate over the entire loop if we found the value
#     i += 1
#
# k = 0

# while k < len(yaz):
#     print(f"#{k + 1} Still searching")
#     if yaz[k] == "Yazan":
#         print(f"Found it: {yaz[k]}")
#         continue
#     k += 1
# If used continue, we skip the lines below and go back to the loop again,
# so it never reaches to k += 1, which will cause
# infinite loop


# Range:

# range(start, stop, step_size)
# By default, the start would be from 0, the step size would be 1 and the stop would be
# When the length is reached

# For Loop
# for iter in sequence:
#     statement
#     statement

for i in range(1, 11, 2):
    print(i)

names = ["Yazan", "Farrah", "Italy", "Europe"]

for name in names:
    print(name)
else:
    print("For loops is done.")

# How to access the index?

for index, item in enumerate(names):
    print(index, item)

# Another way:

name = "Yazan"

for i in range(len(name)):
    print(i, name[i])

# Enumerate is a tuple, it looks like this:

for index, item in [(0, "First"), (1, "Second"), (2, "Third")]:
    print(index, item)
