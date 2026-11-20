# Import the 'Polygon' parent class.
import Polygon

# Define the child 'Triangle' class; again we're making a derived class.
class Triangle(Polygon.Polygon):
    def area(self):
        return (self.width * self.height / 2)