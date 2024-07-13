# # File Handling
#
# # open(filename, mode)
#
# # There are 2 types of file names, absolute and relative
# # Absolute: always begins with the root folder.
# # Relative: where the file is located relative to the program's current working directory
#
#
# # To use absolute format, we start with '/', that means we start looking for directories from the root folder
#
# # Example:
#
# # open('/Users/macbook/PycharmProjects/Giraffe/text.txt')  # This is absolute
# # open('Users/macbook/PycharmProjects/Giraffe/text.txt')  # Relative
#
# # But since notes.py is in the same folder of this file, we can just call it like this:
#
#
# # The mode is:
# # 1. Read
# # 2. Update
# # 3. Write to a file
# # 4. Create
#
# # By default, "r" is set, which is reading if we don't pass it
#
# # open("text.txt", 'r')  Read
# # open("text.txt", 'a')  Append, if it doesn't exist -> create it
# # open("text.txt", 'w')  Write, it also creates a file if it doesn't exist
# # open("text.txt", 'x')  Create, it creates a file and returns an error if the file already exists.
#
#
# file = open('text.txt')
# # print(file.read(3))  # The amount of characters to return (3)
# # If we want to return one line for example:
#
# # print(file.readline())  # First line
# # print(file.readline())  # Second line
#
#
# # If I want to start reading after a specific number of characters:
#
# file.seek(10)
#
# # if we want to print all lines:
#
# for line in file:
#     print(line)
#

# Now to write to it:


# file = open('text.txt', 'w')
#
# # file.read()  Doesn't work because now we are writing to it
#
# file.write('That feels wowzi...')

# file = open('text.txt', 'r+')  # This is for reading and writing together
#
# file.write("OMG")
#
# print(file.read())


# If I want to add a new line and not remove anything:

file = open('text.txt', 'a')  # This is for reading and writing together

file.write("\nAppending stuff to it")

file.close()

# To delete the file, we use the os module

import os

os.remove('text.txt')
