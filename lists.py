names = [1, 2, 3, 4, 5, 6, 1]

# Checking if list is empty or not
if names:
    print("Not empty")
else:
    print("Empty")

# reversing list
# Either like this:
# names = names[::-1]
# Or this:
# names.reverse()


print(names)

# Extracting list variables and assigning them to a variable


num1, num2, num3, num4, num5, num6, num7 = names

print(num1, num2, num3, num4, num5, num6)

# If I wanted to take only one variable and assign it, I can use asterisk *

first_num, second_num, *arr, last_array_element = names

print(first_num, second_num, arr, last_array_element)

print(names.count(1))

names[-1] = "7"

print(names)

# Changing more than one element at the same time in a list:

names[1:2] = ["2nd", "3rd"]

temp = 0

# To get the index of an item that we have its value, we can use this below method or the following one "For loop"

print(names.index("3rd"), "Got the index")

# Used enumerate to get the index in the for loop

for i, name in enumerate(names):
    if name == "3rd":
        temp = i

names.pop(temp)

print(names)

print(names * 3)

print(names.append("Yaz"))  # Returns None
print(names)

names.remove("Yaz")

print(names)

print(names.index("2nd"))

# names.sort()  # Is a method that actually changes the List

# sorted(names)  # While sorted is a function that returns a new list and doesn't modify the original one

# To join a list and make it separated by certain element:

heros_list = ["Bat", "Spider", "Milk", "Iron"]

new_heros = ", ".join(heros_list)

print(new_heros)

# To get new_heros to a list, we use spilt:

new_heros_list = new_heros.split(",")

print(f"new_heros_list: {new_heros_list}")

# Copying a list:

list_2 = ["Hi", "Hola", "Hello", "Salam"]

list_3 = [1, 2, 3, 4, list_2]

new_list = list_3[:]  # This way if we change the list_3 like append to it, this new_list doesn't get effected

print(list_2)
print(list_3)

# list_3 = [1, 2, 3, 4, list_2]
#  Gives us [1, 2, 3, 4, ['Hi', 'Hola', 'Hello', 'Salam']], if we want to get rid of [] in the inner array
# we use extend:

ex_list = [1, 2, 3, 4, 5]

n_list = ["h", "w", "o"]

ex_list.extend(n_list)

print(ex_list)  # [1, 2, 3, 4, 5, 'h', 'w', 'o']
