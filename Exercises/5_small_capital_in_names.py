# Extract the names that have "r"/ "R" in them

names_list = ["Princess", "Madam", "Lady", "Gentleman", "Doctor", "Engineer", "Royal", "Riyad"]

# One line solution with list comprehension

r_list = [item for item in names_list if "r" in item.lower()]

print(r_list)

# Or:

# r_list = []


# for i in names_list:
#     if i.__contains__("r") or i.__contains__("R"):
#         r_list.append(i)
#
# if not r_list:
#     print("List is empty, no r's, R's were found")
# else:
#     print(r_list)

# Or:

# for name in names_list:
#     if "R" in name or "r" in name:
#         r_list.append(name)

# Or with one condition to check for:

# for name in names_list:
#     # name = name.lower() # This would cause them to be printed all in lower, so we do the below instead:
#     if "r" in name.lower():
#         r_list.append(name)
