# Here we are setting a parent class called 'Polygon'. Other shape classes will inherit this class's setup.
class Polygon:

    # Class attributes
    width = 0
    height = 0

    # Class method
    def set_values(self, width, height):
        self.width = width
        self.height = height

    # Another method
    def declare(self):
        print(f"I have a width of {self.width} & a height of {self.height}.")