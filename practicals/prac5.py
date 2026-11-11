'''
#1). Define a class "2DPoint" with x and y coordinates as attributes.
 # Create relevant methods to print the objects.
 # Define a distance() method to calculate the distance between any two point objects.

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point2D(3, 4)
p2 = Point2D(6, 8)
print(p1)
print()
print(p2)
print(f"Distance between {p1} and {p2}: {p1.distance(p2)}")

'''

#2). Inherit the Point2D class to create a Point3D class with an additional attribute z. 
 # Override the distance() method to calculate the distance
 # between two 3D points. Create objects and display them.


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Point3D(Point2D):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, point):
        return ((self.x - point.x) ** 2 +
                (self.y - point.y) ** 2 +
                (self.z - point.z) ** 2) ** 0.5

    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.z})"


p1 = Point3D(3, 4, 5)
p2 = Point3D(6, 8, 9)

print(p1)
print()
print(p2)

print("Distance between", p1, "and", p2, ":", p1.distance(p2))
