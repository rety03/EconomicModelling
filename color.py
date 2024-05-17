from point import Point

import random


class ColoredPoint(Point):
    COLORS = ["red", "blue", "magenta", "purple", "pink"]

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        if color in self.COLORS:
            self.color = color
        else:
            raise Exception(f"That is an invalid color. Accepted colors are {self.COLORS}")

    def __str__(self):
        return f"{self.color} ({self.x}, {self.y})"

    def add_extra_color(self, color):
        self.COLORS.append(color)


p1 = ColoredPoint(10, 10, "red")
# p2 = ColoredPoint(5, 5, "poker")

colored_points = []
for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-10, 10),
                     random.randint(-10, 10),
                     random.choice(ColoredPoint.COLORS))
    )

for i, point in enumerate(colored_points, 1):
    print(f"Colored Point {i}: {point}")

p1.add_extra_color("orange")
p2 = ColoredPoint(3, 4, "orange")
print(p2)
print(f"p2={p2} and has distance to origin={p2.distance_origin()}")