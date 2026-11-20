# Import both the derived (child) classes.
import Rectangle
import Triangle

# Create instances.
rectangle_1 = Rectangle.Rectangle()
triangle_1 = Triangle.Triangle()

# Set their own values using the method defined in the parent class.
rectangle_1.set_values(4, 5)
triangle_1.set_values(8, 10)

# State their areas using the methods defined in thier own respective classes.
print("Rectangle_1 area:\t", rectangle_1.area())
print("Triangle_1 area:\t", triangle_1.area())
print(rectangle_1.declare())
print(triangle_1.declare())