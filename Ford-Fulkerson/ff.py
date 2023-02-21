# Ford-Fulkerson algorith in Python

class Graph:

    def __init__(self, graph):
        self.graph = graph  # original graph
        self.residual_graph = [[cell for cell in row] for row in graph]  # cloned graph
        self.latest_augmenting_path = [[0 for cell in row] for row in graph]  # empty graph with same dimension as graph
        self.current_flow = [[0 for cell in row] for row in graph]  # empty graph with same dimension as graph

    def ff_step(self, source, sink):
        """
        Perform a single flow augmenting iteration from source to sink
        Update the latest augmenting path, the residual graph and the current flow by the maximum possible amount according to your chosen path.
        The path must be chosen based on BFS.
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the amount by which the flow has increased.
        """
        if not self.breadth_first(source, sink):
            return 0

        prev_flow = sum(self.current_flow[source])
        cur_flow = self.get_current_flow()

        self.update_current_flow(cur_flow)
        self.update_residual_graph(cur_flow)

        return sum(self.current_flow[source]) - prev_flow


    def ford_fulkerson(self, source, sink):
        """
        Execute the ford-fulkerson algorithm (i.e., repeated calls of ff_step())
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the max flow from source to sink
        """
        max_flow = 0
        while True:
            cur_flow = self.ff_step(source, sink)
            if cur_flow == 0:
                break
            max_flow += cur_flow

        return max_flow



    def breadth_first(self, source, sink):
        self.latest_augmenting_path = [[0 for cell in row] for row in self.graph]
        graph_range = range(len(self.graph))

        parents = [None for x in graph_range]

        visited = [False for x in graph_range]
        visited[source] = True

        queue = [source]

        while queue:
            v = queue.pop(0)
            for i, neighbor in enumerate(self.residual_graph[v]):
                if not visited[i] and neighbor != 0:
                    visited[i] = True
                    queue.append(i)
                    parents[i] = v

                    if i == sink:
                        parent = parents[sink]
                        while True:
                            self.latest_augmenting_path[parent][i] = 1
                            if parents[parent] is None:
                                break
                            i = parent
                            parent = parents[i]
                        self.latest_augmenting_path[source][i] = 1
                        return parents
        return False



    def get_current_flow(self):
        cur_flow = float('inf')
        for i, row in enumerate(self.latest_augmenting_path):
            for j, col in enumerate(row):
                if col == 1:
                    cur_flow = min(cur_flow, self.residual_graph[i][j])
        return cur_flow

    def update_current_flow(self, cur_flow):
        for i, _ in enumerate(self.graph):
            for j, _ in enumerate(self.graph[i]):
                if self.latest_augmenting_path[i][j] == 1 and self.graph[i][j] == 0:
                    self.current_flow[j][i] -= cur_flow
                elif self.latest_augmenting_path[i][j] == 1:
                    self.current_flow[i][j] += cur_flow

    def update_residual_graph(self, cur_flow):
        for i, _ in enumerate(self.residual_graph):
            for j, _ in enumerate(self.residual_graph[i]):
                if self.latest_augmenting_path[i][j] == 1:
                    self.residual_graph[i][j] -= cur_flow
                    self.residual_graph[j][i] += cur_flow