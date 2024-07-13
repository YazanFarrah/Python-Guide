# Sets:
# Sets can't have the same element duplicated
my_list = [1, 2, 2, 2, 2]  # Works

my_sets = {1, 2, 3, 4, 2}

# It will return 1, 2, 3, 4 without the duplicated 2

print(my_sets)

my_list = set(my_list)

print(my_list)  # Returns only 1, 2

# Note, sets the elements order isn't accurate, like if we put "Hi", 1, 2, 3,
# It might become: 1, 2, 3, "Hi"

sets_order = {"hi", 1, 2, 3}

print(sets_order)

# We can't access element with [num], we have to loop over to get an element

for elem in sets_order:
    print(elem)

# Adding to a set:

sets_order.add(7.1)  # In list, it was called append

print(sets_order)

sets_order.remove("hi")

print(sets_order)

sets_order.pop()  # Removes random element

print(sets_order)

# We can update the set with more than one element using the update method

sets_order.update([5, 4, "3rd"])

print(sets_order)

print(3 in sets_order)  # In this scenario, set is way faster with O(1) time compared to O(n) in lists

first_set = {1, 2, 3, 4, 5}
second_set = {1, 2, 11, 12}

# How to find all elements that are in both of those sets?

common_values = first_set.intersection(second_set)
# Or first_set & second_set

print(common_values)

# Combine sets together: we use union: but remember sets don't allow duplication ;)

union_set = first_set.union(second_set)
# Another way to use union is |
union_set2 = first_set | second_set

print(union_set)
print(union_set2)

# To get the different values between two sets, it checks what values appear in first set and don't appear
# in the second set, "Unique values in the first set compared to the second" "Order matters"

print(first_set.difference(second_set))
print(second_set.difference(first_set))
# We can use the - operator to get the unique values

print(first_set - second_set)

# To get all the differences in sets, we use symmetric_difference

print(first_set.symmetric_difference(second_set))

# To check if a set's elements are all in another one, but the other one maybe has more
# That's called being a subset of another set, we use issubset

sub_set = {1, 2, 3, 4, 5}
super_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(sub_set.issubset(super_set))  # True

print(super_set.issuperset(sub_set))  # True

print(super_set.issubset(sub_set))  # False

print(sub_set.issuperset(super_set))  # False

# To check if there are no common elements between sets:

print(sub_set.isdisjoint(super_set))  # False because there are common elements

not_same1 = {1, 2, 3}
not_same2 = {4, 5, 6}

print(not_same1.isdisjoint(not_same2))  # True
