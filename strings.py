string = "Hello there, this is a sentence"

print(len(string))  # Returns the length of the string

# a way to get the last index of the string:

last_char_index = int(len(string)) - 1

print(string[last_char_index])

# or a much easier way, is by using -1 and so on, I can get the before last by -2 and so on...

print(string[-1])

# Strings are immutable, it means we can't change the value of one index of a string

# name = "Hey"

# name[0] = "i"  # TypeError: 'str' object does not support item assignment

# But, we can do this: but this will create another string not the same one and to prove this, we can use the id()
# from python to prove it

name = "Hey"

print("Before ", id(name))

name = "Hello there"

print("After ", id(name))

print(name)

# Slicing in python is easy, we just use 1 : 3 method, here 1 is included, but 3 isn't, let's say we want to get az
# from Yazan

my_name = "Yazan"

print(my_name[1:3])

# I f I am starting at index 0, I can do it two ways, #1 :  [1: 3]  #2: [:3]

# And if I want to display only two following chars, I can do this: [1:], this will take 1 and 2

# If I do this: [:] it will get the entire string

# If we did this for example: [:100] and there's no 100 indexes, it will still print the entire string without error

# What if I wanted to skip some chars?

# Here I am starting from the first, and take 2 chars, return the first one and skip the second one
print(my_name[::2])

# Here I start from 1 and skip the 2nd from the 2 picked chars as well

print(my_name[1::2])

# If I want to reverse the string, I can easily do it like this:

print(my_name[::-1])

# And if I want to start reversed order but skip chars like the example before

print(my_name[::-2])

# Note, each time a new string was created.

# String interpolation has 3 ways in python:

my_age = 24

string_interpolation = "Hello my name is {}, and I am {} old".format(my_name, my_age)

string_interpolation2 = "Hello my name is {name}, and I am {age} old".format(age=my_age, name=my_name)

string_interpolation3 = f"Hello my name is {my_name}, and I am {my_age} old"

print(string_interpolation)
print(string_interpolation2)
print(string_interpolation3)

pi = 3.14159

print(f"Value of pi is: {pi:.3f}")  # Notice here the value was rounded to 3.142 instead of 3.141, because of the 5
# after 1


small_letter = "hello"

print(small_letter.capitalize())

# To capitalize the first letter of each separated word, we use title

small_words = "this is a title!"

print(small_words.title())

# If there were too many spaces at the beginning and the end, what we do is we use strip

name = "        Yazan          "

name = name.strip()
print(name)

name = name.replace("a", "x")  # This is case-sensitive, if I used "A" instead of "a" it won't replace
# anything since there's no "A" in "Yazan"

print(name)

print(name.count("x"))

print(".".join(name))  # This way I separated all the characters by a "."

# To check if a char or word is in a string, we use "target" in "variable"

new_name = "Laetitia"

print("Lae" in new_name)  # True
print("lae" in new_name)  # False, since it's case-sensitive

print("zack" not in new_name)  # True
