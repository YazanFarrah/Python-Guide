my_tuple = (1, 2, 3, "4")

print(my_tuple[0])

elem1, elem2, elem3, elem4 = my_tuple

print(elem3)

first, *rest = my_tuple
print(first)
print(rest)

rest.append("Hey")

print(rest)

# To convert tuple to a list:

my_tuple = list(my_tuple)

print(my_tuple)

my_tuple = tuple(my_tuple)

print(my_tuple)

# my_tuple.remove(2)  Doesn't work, we can convert it to a list then back to tuple

my_tuple = list(my_tuple)

my_tuple.remove(2)

my_tuple = tuple(my_tuple)

print(my_tuple)

# We can loop over tuples as well

for element in my_tuple:
    print(element)

