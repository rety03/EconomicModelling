import random


class Point:
    def __init__(self, x, y):
        """
        This will be called when instantiating an object
        :param x: the value of x
        :param y: the value of y
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        This will return the string value used in printing the point
        :return:
        """
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """
        This is when the point is in a list or other container
        :return:
        """
        return self.__str__()

    def distance_origin(self):
        """
        calculate the distance to the origin from the point
        :return:
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        define how a point is greater than another
        :param other: the other point to compare against
        """
        return self.distance_origin() > other.distance_origin()


random_points = []

for i in range(5):
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    random_points.append(Point(x, y))

for i, point in enumerate(random_points, 1):
    print(f"Point {i}: ({point.x}, {point.y})")

print("printing point value:", random_points[0])
a = Point(3, 4)
print(f"distance origin a={a.distance_origin()}")

# greatest_point = max(random_points, key=lambda point: point.distance_origin())
# print(f"The greatest point is: {greatest_point} with distance from origin: {greatest_point.distance_origin()}")

random_points.sort()
print(f"The greatest point is: {random_points[-1]} with distance from origin: {random_points[-1].distance_origin()}")
