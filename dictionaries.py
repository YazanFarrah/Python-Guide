# Dictionaries

import operator

grades_in_math = {
    "Yazan": 100,
    "Ahmad": 49,
    "Asem": 82,
    "Zack": 91,
    "Zack": 91,
    #     It will automatically ignore the duplicate and use one only
}

# Another way:
grades = dict(Yazan=100, Ahmad=49, Asem=82, Zack=91)

print(grades)
print(grades_in_math)

print(grades_in_math["Yazan"])
# print(grades_in_math["ASAa"])  # None but with error, in order to safely check for keys, use get :

print(grades_in_math.get("ASAa"))  # None, to return a default value if not exist "None":

print(grades_in_math.get("ASAa", "Default bitch"))

# To add element to dictionary:

grades_in_math["Bitch"] = 0

print(grades_in_math)

# To update, same way of adding if the key exist, it will be updated

grades_in_math["Bitch"] = 10

print(grades_in_math)

grades_in_math.popitem()  # It removes the last item "Bitch"

print(grades_in_math)

# To get all keys of dictionary: use .keys(), to get all values, use .values()

print(grades_in_math.keys(), grades_in_math.values())

# To get them together: use .items(), returns Tuples 

print(grades_in_math.items())

for key in grades_in_math.values():  # Prints all Values
    print(key)

for key in grades_in_math:  # Prints all Keys
    print(key)

for key in grades_in_math.items():  # Prints all Keys and values
    print(key[0], key[1])  # To access the key and the value separately use [0] for key, [1] for value

# Shorter way to unpack the keys and values:

for key, value in grades_in_math.items():
    print(key, value)

fnc = operator.itemgetter(1)

print(sorted(grades_in_math.items(), key=fnc))
