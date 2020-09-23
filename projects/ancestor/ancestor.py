
from graph import Graph

from util import Queue

# Describe the problem in graphs terminology
# What are our nodes?
# What are our edges? if a descendant/parent
# Directed graph

# Build your graph or write get_neighbors()
# Can do either

# Choose your fighter!
# Which algorithm in this situation
# More like a traversal: visit every possible node from your starting node

# Depth vs Breadth
# BF -> shortest path
# DB -> heads to leaves first


def earliest_ancestor(ancestors, starting_node):
    # Create the graph
    graph = Graph()

    # add the pairs to vertices set
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # build edges in reverse, from bottom up
        graph.add_edge(pair[1], pair[0])

    # longest path length
    max_path_len = 1

    # earliest ancestor node
    earliest_ancestor = -1

    # Empty queue
    q = Queue()
    # add starting_node to queue
    q.enqueue([starting_node])

    # while queue is not empty
    while q.size() > 0:

        # dequeue from front of queue
        # this is our current path
        path = q.dequeue()

        # grab current vertex from end of path
        vertex = path[-1]

        if (len(path) >= max_path_len and vertex < earliest_ancestor) or (
            len(path) > max_path_len
        ):
            earliest_ancestor = vertex
            max_path_len = len(path)

        for neighbor in graph.get_neighbors(vertex):
            new_path = list(path)
            new_path.append(neighbor)
            q.enqueue(new_path)

    return earliest_ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
