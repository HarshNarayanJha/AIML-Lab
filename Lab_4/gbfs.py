import heapq


def greedy_best_first_search_graph(graph, h, start, goal):
    opens = []
    heapq.heappush(opens, (h[start], start))

    came_from = {start: (None, 0)}

    visited = set()
    visited.add(start)

    explored = []

    while opens:
        _, curr = heapq.heappop(opens)

        explored.append(curr)

        if curr == goal:
            path = []
            cost = 0
            while curr:
                path.append(curr)
                curr, c = came_from[curr]
                cost += c
            return path[::-1], cost, explored

        if curr in graph:
            for negh, w in graph[curr]:
                if negh not in visited:
                    visited.add(negh)
                    came_from[negh] = (curr, w)

                    h_val = h.get(negh, float("inf"))
                    heapq.heappush(opens, (h_val, negh))

    return None, None, None


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

heuristics = H = {"A": 2, "B": 2, "C": 1, "D": 3, "E": 2, "F": 1, "G": 0, "H": 3}

path, total_cost, explored = greedy_best_first_search_graph(
    adjacency_list, heuristics, "A", "G"
)

if path:
    print(f"Nodes Explored:\t\t[{', '.join(explored or [])}]")
    print(f"Best path from A to G:\t{' -> '.join(path)}")
    print(f"Total Cost:\t\t{total_cost}\n")
