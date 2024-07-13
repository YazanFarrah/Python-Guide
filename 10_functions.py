# Functions
def hello_python(name: str, age=None):
    print(f"Hello from Python, How are you {name}? {str(age).strip() if age else ""}?")


hello_python(name="Yazan", age=25)


# If we want only positional arguments and not allow named arguments, we put / after the last argument:

def hello_postitional(name, age, /):
    print(name, age)


# hello_postitional(name= "Yazan", age = 25)  # Error

hello_postitional("Yazan", 25),  # Correct


# If we put it in between or beginning, only the left arguments can be positional but the right ones can be both

def hello_both(name, /, age, msg) -> None:  # -> The expected return value
    print("Name: ", name, "Age: ", age, "Msg: ", msg)


hello_both("Yazan", age=25, msg="Hola")


def hello_named(*, name, age, msg):  # * To only allow named args, reverse of what's above applies
    print("Name ", name, "Age: ", age, "Msg: ", msg)


hello_named(msg="Hey", age=25, name="Yazan")


# Arbitrary argument to put as many arguments as we need

def arbitrary_argument(*arg):
    print(arg)


arbitrary_argument("Yazan", "Xa", "Ya")


# Arbitrary arguments must be at the last

def my_friends(close, best, *general):
    print("Closest: ", close)
    print("Best: ", best)
    for e in general:
        print(e)


my_friends("Abd", "Amr", "Nour", "Latvi")


def my_friends_other_way(close, best, **general):
    print("Closest: ", close)
    print("Best: ", best)
    print(general)


my_friends_other_way("Abd", "Amr", general1="Nour",
                     general2="Latvi")  # Here general returns dictionary instead of tuple


# I can return more than one value at the same time

def multi_return():
    return "Hello", "Hola"


text1, text2 = multi_return()

print(text1, text2)


def multi_arbitrary(*, name, age, **value):
    print(name)
    print(age)
    print(value)


multi_arbitrary(name="Yazan", age=25, v1="Hello", v2="Hola")


# Nested function

def first_function(name):
    full_name = name + " Farrah"

    def second_function(second_variable):
        print(full_name)

    full_name = name + " Python"
    return second_function


# To understand this, use https://pythontutor.com/ for better understanding

print(first_function("Yazan")("don't care about this value, has been passed only to call the nested function"))


def other_function(name):
    full_name = name + " Farrah"

    def second_function(second_variable):
        print(full_name)

    full_name = name + " Python"
    print(full_name)
    return second_function


variable = other_function

variable("Zack")


def my_func_by_reference(lst: list):
    lst.insert(0, 10)
    for e in lst:
        print(e)


my_list = [20, 30, 40]

my_func_by_reference(my_list)

print(my_list)


def my_func_by_value(val: int):
    val += 20
    print(val)


int_value = 10

my_func_by_value(int_value)

print(int_value)

# The reason why the int_value hasn't been changed like the function before it "my_list" has been changed is because
# Lists or Dictionaries, Sets are passed by reference, unlike Integers, Strings, Float, Tuples, etc... so that's why
# the list was actually modified
