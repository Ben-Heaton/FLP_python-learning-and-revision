# Import the 'Polygon' parent class.
import Polygon

# Define the child 'Rectangle' class; or in other words we're making a derived class.
class Rectangle(Polygon.Polygon):
    def area(self):
        return self.width * self.height