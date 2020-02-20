from points import Point
import random as rd

def kNN(point, points: list, k: int):
    k_points = list()
    return k_points


def main(n, k):

    n_points = [Point(rd.random(), rd.random()) for i in range(n)]
    point = Point(rd.random(), rd.random())
    k_points = kNN(point, n_points, k)
    print("k nearest neighbours of %s are:"%point)
    for p in k_points:
        print(p)


if __name__ == '__main__':
    main(1000, 10)
