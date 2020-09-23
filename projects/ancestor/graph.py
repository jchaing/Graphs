"""
If you can make a function to return the neighbors of this thing, you can treat the problem as a graphs problem

If you can figure out when this item is and is not "related" to other items, graphs problem -> graphs algorithms

1. Describe the problem using graphs terminology
    - What are your nodes?
    - What are your edges? aka when is a node connected to another node
    - Are there connected components?

2. Build your graph OR write your getNeighbors() function

3. Choose your algorithm
    - BFT, DFT, BFS, DFS
"""

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    # Adjacency List Time Complexity: 0(1)
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()


    # Adjacency List Time Complexity: 0(n)
    def delete_vertex(self, vertex_id):
        # delete the key-value pair

        # find all references to this vertex
        pass

    # Adjacency List Time Complexity: O(1)
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    # Adjacency List Time Complexity: O(1)
    def delete_edge(self, v1, v2):
        # access v1, remove v2
        # access v2, remove v1
        pass

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # make a queue
        q = Queue()

        # initial node starting point
        q.enqueue(starting_vertex)

        # make a set to track visited nodes
        visited = set()

        # while queue isn't empty
        while q.size() > 0:

            # dequeue from front of queue
            # this is our current node
            cur_node = q.dequeue()

            # if we have not visited
            if cur_node not in visited:

                # print current node
                print(cur_node)

                # mark as visited
                visited.add(cur_node)

                # get vertex's neighbors
                neighbors = self.get_neighbors(cur_node)

                # put the neighbors in the queue
                for neighbor in neighbors:
                    # print(neighbor)
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # make a stack nodes to visit
        stack = Stack()

        # initial node starting point
        stack.push(starting_vertex)

        # make a set to track visited nodes
        visited = set()

        # while the stack isn't empty
        while stack.size() > 0:

            # pop off top of stack
            # this is our current node
            cur_node = stack.pop()

            # if we have not visited
            if cur_node not in visited:

                # print current node
                print(cur_node)

                # mark as visited
                visited.add(cur_node)

                # get current node's neighbors
                neighbors = self.get_neighbors(cur_node)

                # put current node's neighbors on the stack
                for neighbor in neighbors:
                    stack.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # pass  # TODO
        if visited == None:
            visited = set()

        visited.add(starting_vertex)

        print(starting_vertex)

        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Empty set to store visited nodes
        visited = set()

        # Empty queue
        q = Queue()

        # add starting_vertex to queue
        q.enqueue([starting_vertex])

        # while queue is not empty
        while q.size() > 0:
            # dequeue from front of queue
            # this is starting path
            path = q.dequeue()

            # grab current vertex from end of path
            vertex = path[-1]

            # if vertex not visited
            if vertex not in visited:
                # if vertex is destination_vertex
                if vertex == destination_vertex:
                    # return current path
                    return path

            # add neighbors to queue
            for neighbor in self.get_neighbors(vertex):
                # create new path
                new_path = list(path)
                # add neighbor to new path list
                new_path.append(neighbor)
                # queue new path list
                q.enqueue(new_path)

        return "BFS not found"

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # Empty set to store visited nodes
        visited = set()

        # Empty stack
        stack = Stack()

        # add starting_vertex to stack
        stack.push([starting_vertex])

        # while stack isn't empty
        while stack.size() > 0:
            # pop off top of stack
            # this is current path
            path = stack.pop()

            # grab vertex from end
            vertex = path[-1]

            # if vertex not visited yet
            if vertex not in visited:
                # if vertex = destination vertex
                if vertex == destination_vertex:
                    # return current path
                    return path
                # mark vertex as visited
                visited.add(vertex)

            # Add neighbors to the stack
            for neighbor in self.get_neighbors(vertex):
                # new path
                new_path = list(path)
                # append neighbors to new path
                new_path.append(neighbor)
                # add new path to stack
                stack.push(new_path)

        return "DFS: Value not found"


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # pass  # TODO

        if len(path) == 0:
            path.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path

        visited.add(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)

        if len(neighbors) == 0:
            return None

        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = path + [neighbor]
                result = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)

                if result is not None:
                    return result

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
