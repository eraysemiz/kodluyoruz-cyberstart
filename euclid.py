from math import sqrt

points = [(1, 5), (3, 7), (9, 1), (5, 2)]
distances = []


def euclideanDistance(x, y):
    euclid = sqrt(((y[0] - x[0]) ** 2) + ((y[1] - x[1]) ** 2))
    return euclid


for x in points:
    for y in points:
        if x == y:
            continue
        else:
            distances.append(euclideanDistance(x, y))

print(min(distances))
