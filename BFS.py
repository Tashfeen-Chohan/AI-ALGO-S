from collections import deque

def bfs(graph, start):
    visited = set()          # A set to keep track of visited nodes
    queue = deque([start])   # Initialize the queue with the start node
    
    while queue:             # Continue until the queue is empty
        vertex = queue.popleft()  # Dequeue a node from the front of the queue
        if vertex not in visited:
            visited.add(vertex)   # Mark the node as visited
            print(vertex)         # Process the node (e.g., print it)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor) # Enqueue unvisited neighbors

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

bfs(graph, 'A')
