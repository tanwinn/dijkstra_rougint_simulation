"""
    CS330 Final Project: Routing Algorithm
    Professor Visa
    Thanh Nguyen & Thomas Matlak
    Distance Vector Algorithm
    Written by Thanh Nguyen
"""

import sys, queue
from dijkstra_routing import parse_graph_file, print_routing_table


class Graph:
    def __init__(self, vertex, src = 0):
        self.v = vertex
        self.graph = []
        self.src = src # src node

    def isSrc(self, src):
        self.src = src

    def addEdge(self, tuple):
        # undirected graph
        self.graph.append(tuple)
        self.graph.append(tuple)

    def printGraph(self, distance):
        # print the solution
        print("From source: ", self.src)
        print("Node |  Distance")
        for i in range(self.v):
            print(" ", i, "     ", distance[i])


def BellmanFord(graph):
    infi = float("Inf")
    distance = [infi] * graph.v
    distance[graph.src] = 0
    prev = [None for _ in range(graph.v)]
    print(prev)
    for i in range((graph.v-1)*2):
        for u, v in graph.graph:
            if distance[u] != infi and distance[u] + 1 < distance[v]:
                distance[v] = distance[u] + 1
                prev[v] = u
    # graph.printGraph(distance)
    return distance, prev


def main():
    """
    read in the txt file of the graph
    :return: print out routing table for assigned node
    """
    input_file = "default_graph.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    vertices, edges = parse_graph_file(input_file)
    G = Graph(len(vertices))
    for e in edges:
        G.addEdge(e)

    # build routing table
    for v in vertices:
        G.isSrc(v)
        dist, prev = BellmanFord(G)
        print(dist, prev)


if __name__ == '__main__':
    main()

# def DistanceVector(graph):
#     distance = float(["Inf"]) * graph.v
#     distance[graph.src] = 0
#     for x in graph.vertex:

