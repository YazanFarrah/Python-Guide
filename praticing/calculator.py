num1 = float(input("Enter 1st num\t"))
num2 = float(input("Enter 2nd num\t"))


function = input("please enter either +, -, *, /\t")


if function == "+":
    print(float(num1 + num2))
elif function == "-":
    print(float(num1 - num2))
elif function == "*":
    print(float(num1 * num2))

elif function == "/":
    print(num1/num2)
else:
    print("Wrong input")

