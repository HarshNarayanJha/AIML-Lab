class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        H = {"A": 2, "B": 2, "C": 1, "D": 3, "E": 2, "F": 1, "G": 0, "H": 3}

        return H[n]

    def astar(self, start, end):
        explored = []
        opens = set([start])
        closed = set()

        g = {}
        g[start] = 0

        parents = {}
        parents[start] = start

        while opens:
            n = None

            for v in sorted(opens):
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            explored.append(n)

            if n is None:
                print("No path exists")
                return None, None, []

            if n == end:
                relpath = []
                cost = 0

                while parents[n][0] != n:
                    relpath.append(n)
                    cost += parents[n][1]
                    n = parents[n][0]

                relpath.append(start)
                relpath.reverse()

                return relpath, cost, explored

            for m, weight in self.get_neighbors(n):
                if m not in opens and m not in closed:
                    opens.add(m)
                    parents[m] = (n, weight)
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = (n, weight)

                        if m in closed:
                            closed.remove(m)
                            opens.add(m)

            opens.remove(n)
            closed.add(n)

        print("No path!")
        return None, None, []


adjacency_list = {
    "A": [("B", 1), ("C", 1)],
    "B": [("A", 3), ("C", 2), ("D", 1), ("E", 1), ("F", 1)],
    "C": [("A", 3), ("B", 2), ("D", 1), ("E", 1), ("F", 1)],
    "D": [("B", 3), ("C", 3), ("E", 2), ("F", 2), ("H", 1)],
    "E": [("B", 3), ("C", 3), ("D", 2), ("F", 2), ("H", 1)],
    "F": [("B", 3), ("C", 3), ("D", 2), ("E", 2), ("G", 3), ("H", 1)],
    "G": [],
    "H": [("D", 3), ("E", 3), ("F", 3)],
}

graph = Graph(adjacency_list)
path, total_cost, explored = graph.astar("A", "G")

if path:
    print(f"Nodes Explored:\t\t[{', '.join(explored or [])}]")
    print(f"Best path from A to G:\t{' -> '.join(path)}")
    print(f"Total Cost:\t\t{total_cost}\n")
