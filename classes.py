# Using classes to calculate the area of a rectangle, circle, square and the 
# volume of a sphere
pi = 3.142
class  area_rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        return area
    
class area_circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        area = pi * self.radius ** 2
        return area
    
class area_square:
    def __init__(self, side):
        self.side = side
    def area(self):
        area = self.side ** 2
        return area
    
class volume_sphere:
    def __init__(self, radius):
        self.radius = radius
    def volume(self):
        volume = (4 / 3) * pi * self.radius ** 3
        return volume
    
# Instantiating

rectangle = area_rectangle(10, 7)
print("The area of the rectangle is: ", rectangle.area())

circle = area_circle(14)
print("The area of the circle is: ", circle.area())

square = area_square(5)
print("This is the area of the square: ", square.area())

sphere = volume_sphere(7)
print("The volume of the sphere is: ", sphere.volume())
