# # Classes
#
# class PassClass:
#     pass
#
#
# pass_object = PassClass()
#
#
# # Pass is a keyword in python used to don't get errors from python for not putting logic inside the class so far
#
# class Car:
#     # If I want to have static methods or variables that can be accessed without creating an object or with:
#     static_value = "Static :p"
#
#     def __init__(self, *, name, model):
#         self.name = name
#         self.model = model
#         self.doors = 4  # Default value that will not be passed
#
#     def details(self):  # Self here is like "this" keyword in other programming languages
#         print(self.name, self.model)
#
#     def __add__(self, other):
#         print(other.name)
#         return self.name + " " + other.name
#
#     def __str__(self):
#         # Here in str, there must be return and of type str
#         return self.name + " " + str(self.model)
#
#
# car = Car(name="BMW", model=2024)
#
# print(car.model)  # 2024
#
# car.details()
#
# # To modify an object:
#
# car.model = 2025
#
# car.details()
#
# print(Car.static_value)
# # Or:
# # print(Car().static_value)  # But because I have the init function, this won't work because I have to define values
#
# # Using the new __add__ in the class:
#
# second_car = Car(name="Porsche", model=2021)
#
# print(car + second_car)  # I get Porsche printed here because the + is printing other.name, and I get the return as
# # self.name + other.name
#
#
# print(second_car)  # In order to print the car info for example without having to pass car.details, we can use the
# # __str__ dunder method


# Advanced Car class:

class Car:
    def __init__(self):
        self.engine = Engine()

    # This is known as composition, a class instantiated as an instance attribute in another class, I am composing a
    # car with engine inside of it

    def start(self):
        print("Car is starting")
        self.engine.start()


class Engine:
    def start(self):
        print("Engine Started.")


Car().start()
