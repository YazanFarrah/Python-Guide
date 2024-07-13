# You are tasked with implementing a class representing a basic geometric shape.
# The class should support the following operations:
# - Initialization based on variable number of sides.
# - Calculation of the perimeter of the shape.
# - Comparison of two shapes based on their perimeters.


class GeometricShape:
    def __init__(self, *sides):
        self.sides = sides

    def parameter(self):
        parameter_sum = 0

        for side in self.sides:
            parameter_sum += side

        return parameter_sum

    def __eq__(self, other):
        # The below condition returns true or false if the other is an instance of the GeometricShape class
        if isinstance(other, GeometricShape):
            return self.parameter() == other.parameter()
        elif isinstance(other, int):
            return self.parameter() == other
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, GeometricShape):
            return self.parameter() < other.parameter()
        elif isinstance(other, int):
            return self.parameter() == other
        else:
            return False


triangle = GeometricShape(1, 2, 3)
square = GeometricShape(4, 4, 4, 4)

print(triangle == square)
print(triangle < square)
print(triangle < 5)
print(square < 15)

