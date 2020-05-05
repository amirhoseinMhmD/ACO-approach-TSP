import math
import csv

from aco import ACO, Graph
from plot import plot
import time


def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def main():
    cities = []
    points = []
    with open('./data/data_12.txt') as f:
        for line in f.readlines():
            city = line.split(' ')
            cities.append(dict(index=int(city[0]), x=int(city[1]), y=int(city[2])))
            points.append((int(city[1]), int(city[2])))
    cost_matrix = []
    rank = len(cities)
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)
    aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 2)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)
    make_csv('{}, path: {}'.format(cost, path), 'result.csv')
    print('cost: {}, path: {}'.format(cost, path))


    # plot(points, path)


def make_csv(data, file_name):
    """
    Writes data to csv file.
    """
    with open(file_name, 'a') as f:
        f.write(data)
        f.write('\n')
        # writer = file.writer(f)
        # writer.writerow(data)
    f.close()


if __name__ == '__main__':
    for i in range(0,2000):
        start_millis = int(round(time.time() * 1000))
        main()
        time.time()
        final_millis = int(round(time.time()) * 1000)
        t = final_millis - start_millis
        if t<0:
            t*=-1
        fi = open("times.csv", 'a')
        fi.write(str(t))
        fi.write('\n')
        fi.close()

