import heapq

def ucs(graph, start, goal):
    # Priority queue: elements are tuples of (cumulative cost, current node, path)
    queue = [(0, start, [start])]
    visited = set()  # To keep track of visited nodes

    while queue:
        cost, node, path = heapq.heappop(queue)  # Pop the node with the smallest cost

        if node not in visited:
            visited.add(node)

            if node == goal:  # Goal check
                return path, cost

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return None, float('inf')  # Return None and infinite cost if no path is found

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

path, cost = ucs(graph, 'A', 'J')
print("Path:", path)
print("Cost:", cost)
