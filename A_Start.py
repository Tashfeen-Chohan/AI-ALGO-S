import heapq

def astar(graph, start, goal, heuristic):
    # Priority queue: elements are tuples of (f_cost, g_cost, current node, path)
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()  # To keep track of visited nodes

    while queue:
        h_cost, g_cost, node, path = heapq.heappop(queue)  # Pop the node with the smallest f_cost

        if node not in visited:
            visited.add(node)

            if node == goal:  # Goal check
                return path

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    # Calculate g_cost and f_cost for the neighbor
                    neighbor_g_cost = g_cost + weight
                    neighbor_f_cost = neighbor_g_cost + heuristic[neighbor]

                    # Push neighbor onto the queue with its f_cost, g_cost, and updated path
                    heapq.heappush(queue, (neighbor_f_cost, neighbor_g_cost, neighbor, path + [neighbor]))

    return None  # Return None if no path is found

# Example usage
graph = {
    'S': [('A', 3), ('B', 6)],
    'A': [('C', 2), ('D', 3)],
    'B': [('C', 1), ('E', 5)],
    'C': [('D', 1), ('E', 3)],
    'D': [('G', 2)],
    'E': [('G', 5)],
    'G': []
}

# Heuristic costs (example values)
heuristic = {
    'S': 10,
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 2,
    'G': 0
}

path = astar(graph, 'S', 'G', heuristic)
print("Path:", path)