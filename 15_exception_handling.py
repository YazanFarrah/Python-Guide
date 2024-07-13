# # open('fake_path')  this returns error, to handle it:
#
# try:
#     # open('fake_path')
#     print(0 / 0)
#
# except ZeroDivisionError as error:
#     # If I want to get the exception message, I use as e
#     print("You can't divide by zero ---", error)
# # Order matters here, we leave the general except to the last; or we get an error
# except:
#     print("Wrong path")
#

# How to raise our own errors:   "note raise is like throw"

def divide_nums(a, b):
    if b == 0:
        raise ValueError("Can't divide by zero you dum dum!")
    return a / b


try:
    divide_nums(12, 1)

except ValueError as error:
    print("Error,", error)

else:
    # This gets executed if no error happened :)
    print("No error!")
finally:
    print("This will always run no matter if error of success ;)")
