from typing import Dict, List, Tuple, Mapping, Union

from graph import Graph
from vertex import Vertex
from step import Step


class JKUMap(Graph):
    """
    A class representing a map of the JKU campus.
    """

    def __init__(self):
        super().__init__()
        # Initiaite Points of Interests as vertices
        poi = ['Spar', 'LIT', 'Porter', 'Open Lab', 'KHG', 'Bank', 'Parking', 'Chat', 'Bella Casa', 'Library', 'LUI', 'Teichwerk', 'SP1', 'SP3', 'Papaya',
               'Castle', 'JKH']
        _verts = [self.insert_vertex(p) for p in poi]

        # Create Edges based on distances [given in the assignment pdf]
        edge_raw = [[0,1,50], [0,2,103], [0,4,165], [1,2,80], [2,3,70], [2,5,100], [4,5,150], [4,6,190], [5,7,115], [6,8,145], [6,12,240], [7,9,160],
                    [7,10,240], [9,10,90], [10,11,135], [10,12,175], [12,13,130], [14,15,85], [14,16,80]]
        _edges = [self.insert_edge(_verts[e[0]], _verts[e[1]], e[2]) for e in edge_raw]

        self.distances, self.paths = self._initialize_dijkstra()
        for vertex, _ in zip(self.distances, self.paths):
            self.distances[vertex], self.paths[vertex] = self._dijkstra(vertex, set(), self.distances[vertex], self.paths[vertex])

    def _initialize_dijkstra(self):
        distances = {vertex: {inner_vertex: float("inf") if vertex != inner_vertex else 0 for inner_vertex in self.vertices} for vertex in self.vertices}
        paths = {vertex: {inner_vertex: [] for inner_vertex in self.vertices} for vertex in self.vertices}
        return distances, paths

    def get_shortest_path_from_to(self, from_vertex: Vertex, to_vertex: Vertex) -> List[Step]:
        """
        This method determines the shortest path between two POIs "from_vertex" and "to_vertex".
        It returns the list of intermediate steps of the route that have been found
        using the dijkstra algorithm.
        :param from_vertex: Start vertex
        :param to_vertex:   Destination vertex
        :return:
           The path, with all intermediate steps, returned as a list. This list
           sequentially contains each vertex along the shortest path, together with
           the already covered distance (see example on the assignment sheet).
           Returns None if there is no path between the two given vertices.
        :raises ValueError: If from_vertex or to_vertex is None, or if from_vertex equals to_vertex
        """
        self.validate_empty(from_vertex)
        self.validate_empty(to_vertex)
        if from_vertex == to_vertex:
            raise ValueError('Vertices should not be equal')

        result = self.paths[from_vertex][to_vertex]
        return result if len(result) > 0 else None

    def get_steps_for_shortest_paths_from(self, from_vertex: Vertex) -> Dict[str, int]:
        """
        This method determines the amount of "steps" needed on the shortest paths
        from a given "from" vertex to all other vertices.
        The number of steps (or -1 if no path exists) to each vertex is returned
        as a dictionary, using the vertex name as key and number of steps as value.
        E.g., the "from" vertex has a step count of 0 to itself and 1 to all adjacent vertices.
        :param from_vertex: start vertex
        :return:
          A map containing the number of steps (or -1 if no path exists) on the
          shortest path to each vertex, using the vertex name as key and the number of steps as value.
        :raises ValueError: If from_vertex is None.
        """
        self.validate_empty(from_vertex)
        return {vertex.name: len(self.paths[from_vertex][vertex]) - 1 for vertex in self.vertices}

    def get_shortest_distances_from(self, from_vertex: Vertex) -> Dict[Vertex, float]:
        """
        This method determines the shortest paths from a given "from" vertex to all other vertices.
        The shortest distance (or -1 if no path exists) to each vertex is returned
        as a dictionary, using the vertex name as key and the distance as value.
        :param from_vertex: Start vertex
        :return
           A dictionary containing the shortest distance (or -1 if no path exists) to each vertex,
           using the vertex name as key and the distance as value.
        :raises ValueError: If from_vertex is None.
        """
        self.validate_empty(from_vertex)
        return {key.name: value if value != float("inf") else -1 for key, value in self.distances[from_vertex].items()}

    def _dijkstra(self, cur: Vertex, visited: set, distances: Dict[Vertex, Union[float, int]], paths: Dict[Vertex, List],):
        """
        This method is expected to be called with correctly initialized data structures and recursively calls itself.
        :param cur: Current vertex being processed
        :param visited: Set which stores already visited vertices.
        :param distances: Dict (nVertices entries) which stores the min. distance to each vertex.
        :param paths: Dict (nVertices entries) which stores the shortest path to each vertex.
        """
        visited.add(cur)
        for adj_vert in self.get_adjacent_vertices(cur):
            if adj_vert not in visited:
                actual_distance = self.find_edge(cur, adj_vert).weight
                if (distances[adj_vert] > distances[cur] + actual_distance):
                    distances[adj_vert] = (distances[cur] + actual_distance)
                    if len(paths[cur]) == 0:
                        paths[cur] = [Step(cur, distances[cur])]
                    paths[adj_vert] = paths[cur] + [Step(adj_vert, distances[adj_vert])]

        for neighbor in sorted(distances, key=distances.get):
            if neighbor not in visited:
                return self._dijkstra(neighbor, visited, distances, paths)
        return distances, paths

    def validate_empty(self, v):
        if v is None:
            raise ValueError('Variable should not be empty')