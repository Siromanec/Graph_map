from __future__ import annotations
from graph import Graph
import re
from dfs import DFS_complete
from bfs import BFS_complete
from topological_sort import topological_sort
def read_file(file):
    info = {}
    with open(file, 'r') as file_contents:
        data = file_contents.readline()
        while data:
            data = file_contents.readline()
            res = re.search(r'^(\w+) \((((\w*)[, ]*)*)\)$', data)
            if res is not None:
                if 'none' in res[2]:
                    info[res[1]] =  [None]
                else:
                    info[res[1]] = res[2].split(', ')
                #print(res[1], res[2].split(', '))
    return info
def turn_into_graph(info):
    map_graph = Graph()
    name_to_object = {}
    for child_node in info:
        name_to_object[child_node] = map_graph.insert_vertex(child_node)
    for child_node in info:
        for parent_node in info[child_node]:
            if parent_node:
                map_graph.insert_edge(name_to_object[parent_node], name_to_object[child_node])
                #map_graph.insert_edge(name_to_object[child_node], name_to_object[parent_node])

    return map_graph

def dfs_test(g):
    print([(i.endpoints()[0].element(), i.endpoints()[0].element()) for i in g.edges()])
    print("Number of vertices is", g.vertex_count())
    #print("Vertices is", g.vertices())
    print("Number of edges is", g.edge_count())

    forest = DFS_complete(g)
    print(forest)
    print()
    # for tree in forest:
    #     print(tree, forest[tree])

def bfs_test(g):
    print([(i.endpoints()[0].element(), i.endpoints()[0].element()) for i in g.edges()])
    print("Number of vertices is", g.vertex_count())
    #print("Vertices is", g.vertices())
    print("Number of edges is", g.edge_count())

    forest = BFS_complete(g)
    print(forest)
    print()

    # for tree in forest:
    #     print(tree, forest[tree])

def topological_sort_test(g):
    print("Number of vertices is", g.vertex_count())
    print("Number of edges is", g.edge_count())
    topo = topological_sort(g)
    print("Topo order", [str(v) for v in topo])

if __name__ == '__main__':
    info = read_file('stanford_cs.txt')
    g = turn_into_graph(info)
    dfs_test(g)
    bfs_test(g)
    topological_sort_test(g)