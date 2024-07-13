# oop

# Inheritance

class Wood:
    def __init__(self):
        self.color = 'Red'
        self.origin = 'Africa'


class Table(Wood):
    def __init__(self):
        # Here I have modified the color for this class, but in order to now inherit the parent since we have __init__ here.
        # We need to use the keyword super()

        super().__init__()
        self.color = "Brown"


wood = Wood()

table = Table()

print("Wood class:")
print(wood.color)
print(wood.origin)
print("----------------------")
print("Table class:")
print(table.origin,
      end=" \"This was modified\"\n")  # Africa since it's calling the super class and hasn't been modified
print(table.color)  # Brown since it has been modified


# Polymorphism

# Poly means "many" and morph means "forms"  => Having many forms


class Parent:
    def __init__(self):
        self.eye_color = 'Green'
        self.blood_type = 'A+ve'

    def move(self):
        print('Moving')


class Child:
    def __init__(self):
        self.eye_color = 'Brown'

    def move(self):
        print('Moving Slowly')


# The idea here is that we can execute the same method for both of those classes while the implementation is different
# for both of them

print(Parent().move())
print(Child().move())


# Encapsulation

# The concept of bundling data and methods within single unit
# it's like when we create a class and define methods/functions for it, for example move(), but there's more
# like hiding the method from outside, so it can't be accessed
# For example here I will make sure that the eye_color is private and not accessible from outside the class
# I will do this by putting __ at the beginning indication private property
# For protected: we use only _ underscore, protected means the children classes can access it

class Parent:
    def __init__(self):
        self.__eye_color = 'Green'
        self.blood_type = 'A+ve'
        self._protected = "This is protected"

    def move(self):
        print('Moving')


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.eye_color = 'Brown'

        print(self._protected)

    def move(self):
        print('Moving Slowly')


child_instance = Child()
