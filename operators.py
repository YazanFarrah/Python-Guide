# Arithmetic Operators

# Note: when using normal division, if the variables are int, still the answer would be in decimal, like 6 / 2 = 3.0
# while other operations don't do that.

x = 10
y = 15

# Mod operation:

print(x % y)

# Normal division

print(x / y)

# Floor division:

print(x // y)  # Normal division would give around 0.6666, while floor would give 0

# Normal multiplication

print(x * y)

# Exponents Operation:

print(x ** y)  # 10 ^ 15

# Operations with Strings!

name = "Yazan"

print(f"{name} " * 3)  # Yazan Yazan Yazan

# While a string with a string doesn't work

# print(name * "Hello") # Error can't multiply sequence by non-int of type 'str'

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Assignment Operators:

X = 10

x += 4  # x = 10 + 4 => 14

print(x)

x *= 3  # 30

print(x)

y = 10

y //= 4  # 2.5 => floored => 2

print(y)

# And this applies to / % etc...

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Relational Operators


age = 18

age2 = 25

print(age == age2)  # False

print(age != age2)  # True

# >=  |  <=  >  |  <  |  ==  |  !=

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Logical Operators: and, or, not

name = bool("Yazan")
age = bool(25)

print(name and age)  # True because both are true

zero = bool(0)
one = bool(1)

print(zero)  # False

print(one)  # True

true = True

false = False

print(not (true and false))  # (true and false) => false .. not (false)  => true

# We can use or, etc. but we already got the idea

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Identity Operators, We check if the two variables refers to the same object in memory or not.

age = 18

age2 = 20

print(age is age2)  # False

print(age is not age2)  # True

age3 = age

print(age is age3)  # True because both refer to the same address in memory.

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Membership Operators, in, not in

name = "Yaz"

print("a" in name)  # True

print("a" not in name)  # False

# Membership operators can't be used with numbers

# Relational Operators "Extra"

name = "Yazan"

print(name > "rrr")  # False, why? Because here the comparison is being done with ASCI,
# It compares each character for example "Y" with "r" etc... just forget about it...


# Unary Operators

print(-5 ** 2)  # Expected output is 25 since -5 ^ 2 = 25

# But no, because python here gives the priority to ** and then it adds the negative sign, so we get -25

# If we want to get 25 we do this:

print((-5) ** 2)
