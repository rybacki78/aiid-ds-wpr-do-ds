# Zadania 1,2,3,4,5,7
# to-do Zadanie 6


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __mul__(self, other: int):
        # self * other
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        raise TypeError("Other must be an int")

    def __rmul__(self, other: int):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Point):
            if (self.x == other.x) and (self.y == other.y):
                return True
            else:
                return False
        return False


class Polygon:

    def __init__(self):
        self.points = []

    def add_point(self, p: Point):
        self.points.append(p)

    def __getitem__(self, key):
        if isinstance(key, int):
            if key > len(self.points) - 1:
                raise TypeError("Key value out of bounds")
            else:
                return self.points[key]
        elif isinstance(key, slice):
            return self.points[key]
        raise TypeError("Key must be an int")


p1 = Point()
p2 = Point(3, 4)
p3 = Point()
p4 = Point(9, 9)

print(p1)  # nasz __init__
print(p2)
print(p2 * 3)  # nasz __mul__
print(3 * p2)  # nasz __rmul__
print(p1 == p3)  # nasz __eq__

pol = Polygon()
pol.add_point(p2)
pol.add_point(p3)
pol.add_point(p4)

print(pol[0:])
