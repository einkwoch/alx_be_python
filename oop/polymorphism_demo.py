import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError("derived classes need to override this method")
    

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        super().__init__()

    def area(self):
        return self.length*self.width
        
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__()

    def area(self):
        return (math.pi * (self.radius**2))
    

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()