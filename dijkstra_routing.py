#!/usr/bin/python3

'''
Thomas Matlak and Thanh Nguyen
Network routing with Dijkstra's algorithm

The provided graph is assumed to be connected
'''


import math
import sys
import queue

def parse_graph_file(filename):
    '''
    The first line of an input file is the number of vertices, v
    The second line is the number of edges, e
    The next e lines contain pairs of adjacent vertices
    '''
    vertices = []
    edges = []
    with open(filename, 'r') as infile:
        n_vertices = int(infile.readline())
        n_edges = int(infile.readline())

        for _ in range(n_edges):
            edges.append(tuple(int(v.strip()) for v in infile.readline().split()))

    vertices = [v for v in range(n_vertices)]

    return vertices, edges


def dijkstra(src, vertices, edges):
    '''
    Perform Dijkstra's shortest path algorithm on the graph consisting of vertices and edges
    Uses src as the starting point
    '''

    dist = [(v, math.inf) for v in vertices]
    prev = [None for _ in vertices]

    dist[src] = (src, 0)

    Q = []
    for v in vertices:
        Q.append(v)

    while len(Q) > 0:
        u = sorted(dist, key=lambda v: v[1])[len(vertices) - len(Q)][0]
        Q.remove(u)

        for e in edges:
            if u == e[0]:
                v = e[1]
            elif u == e[1]:
                v = e[0]
            else:
                continue

            alt = dist[u][1] + 1  # if using a weighted graph, change from 1 to the edge weight
            if alt < dist[v][1]:
                dist[v] = (v, alt)
                prev[v] = u

    return dist, prev


def print_routing_table(source, routing_table):
    '''
    Print the routing table for node source
    '''

    print("Routing Table for Node {}\n------------------------".format(source))
    print("DEST | LINK\n-----------")
    for key in routing_table.keys():
        for n in routing_table[key]:
            print("{}    |({},{})".format(n, source, key))
    print("\n")


def main():
    """
    Reading the graph from txt file
    Perform djikstra algorithm with assigned vertex
    :return: print out the routing table for the network
    """
    input_file = "default_graph.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    vertices, edges = parse_graph_file(input_file)

    for v in vertices:
        dist, prev = dijkstra(v, vertices, edges)

        # build routing table
        routing = {}

        Q = queue.Queue()

        for i in vertices:
            Q.put(i)

        while not Q.empty():
            n = Q.get()

            if n == v:
                continue  # we don't need to put the current node in the routing table
            elif prev[n] == v:
                routing[n] = [n]
            elif prev[n] in routing.keys():
                routing[prev[n]].append(n)
            else:
                found = False
                for key in routing.keys():
                    if prev[n] in routing[key]:
                        found = True
                        routing[key].append(n)
                        break
                if not found:
                    Q.put(n)  # keep trying until n's prev is in the routing table

        print_routing_table(v, routing)


if __name__ == '__main__':
    main()
