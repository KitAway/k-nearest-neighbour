from points import Point
import random as rd

def distances(point, points: list):
    pair = list()
    for p in points:
       pair.append((p, p.distance(point)))
    return pair

def minK(pairs, k:int):
    sortD =sorted(pairs, key=lambda x: x[1])
    k_pairs = sortD[:k]
    return [p for p, v in k_pairs]

def kNN(point, points: list, k: int):
    dis = distances(point, points)
    k_points = minK(dis, k)
    return k_points


def main(n, k):

    n_points = [Point(i, i**1.4) for i in range(n)]
    point = Point(2, 8)
    k_points = kNN(point, n_points, k)
    print("k nearest neighbours of %s are:"%point)
    for p in k_points:
        print(p)


if __name__ == '__main__':
    main(1000, 10)
