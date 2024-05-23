import heapq

def best_first_search(graph, start, goal, heuristic):
    # Priority queue: elements are tuples of (heuristic cost, current node, path)
    queue = [(heuristic[start], start, [start])]
    visited = set()  # To keep track of visited nodes

    while queue:
        h_cost, node, path = heapq.heappop(queue)  # Pop the node with the smallest heuristic cost

        if node not in visited:
            visited.add(node)

            if node == goal:  # Goal check
                return path

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None  # Return None if no path is found

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1), ('G', 7)],
    'D': [('H', 3)],
    'E': [('I', 2)],
    'F': [('J', 3)],
    'G': [('K', 1)],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

# Heuristic costs (example values)
heuristic = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 5,
    'F': 4,
    'G': 3,
    'H': 2,
    'I': 1,
    'J': 0,
    'K': 9
}

path = best_first_search(graph, 'A', 'J', heuristic)
print("Path:", path)
