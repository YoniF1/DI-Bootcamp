import math
import turtle

class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2*radius

    def area(self):
        return math.pi * (self.radius * self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        if isinstance(other, Circle):
            if self.radius > other.radius:
                return True       
            else:
                return False
        else:
            Exception("You are comparing to a non Circle")
            
    def __eq__(self, other):
        if isinstance(other, Circle):
            if self.radius == other.radius:
                return True       
            else:
                return False
        else:
            Exception("You are comparing to a non Circle")


c = Circle(100)
d = Circle(200)
print(dir(c))
print(c.__dict__)

a = c.area()
print(a)

e = c + d
print(e)
print(e.radius)

e = c > d
print(e)

e = d > c
print(e)

e = d == c
print(e)

sorted = []
sorted.append(c)
sorted.append(d)
sorted.sort()
for circle in sorted:
    print(circle.radius)

draw = turtle.Turtle()
draw.circle(c.radius)
draw.circle(d.radius)

turtle.done()
