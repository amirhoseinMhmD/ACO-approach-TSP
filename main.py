import math

from aco import ACO, Graph
import time


def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def main():
    cities = []
    points = []
    with open('zi929.tsp') as f:
        for line in f.readlines():
            city = line.split(' ')
            cities.append(dict(index=int(city[0]), x=float(city[1]), y=float(city[2])))
            points.append((float(city[1]), float(city[2])))
    cost_matrix = []
    rank = len(cities)
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)
    aco = ACO(10, 100, 0.99, 10.0, 0.5, 10, 2)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)
    make_csv('{}, path: {}'.format(cost, path), 'result.csv')
    print('cost: {}, path: {}'.format(cost, path))




def make_csv(data, file_name):
    with open(file_name, 'a') as f:
        f.write(data)
        f.write('\n')
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

