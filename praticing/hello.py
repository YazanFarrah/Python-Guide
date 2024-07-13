from math import *

text = "Hello"
text2 = "there"

text3 = text.__add__(" " + text2.capitalize())

print(text3)

text3 = text3.replace(text, "Bitch is")

print(text3)

text4 = "-123"

print(abs(int(text4)))

print(pow(3, 2))  # 3^2 = 9

print(min(3, 10))
print(max(3, 10))


def max_number(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


print(round(3.4))  # returns  0.5=> highest, less than 0.5=> the lowest possible number
print(floor(3.9))  # returns the lowest possible number
print(ceil(3.1))   # returns the highest possible number
print(sqrt(4))   # returns the square root.


