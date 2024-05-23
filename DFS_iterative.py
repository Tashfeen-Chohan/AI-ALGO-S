def dfs_iterative(graph, start):
    visited = set()          # A set to keep track of visited nodes
    stack = [start]          # Initialize the stack with the start node
    
    while stack:             # Continue until the stack is empty
        vertex = stack.pop() # Pop a node from the stack
        if vertex not in visited:
            visited.add(vertex)   # Mark the node as visited
            print(vertex)         # Process the node (e.g., print it)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor) # Add unvisited neighbors to the stack

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

dfs_iterative(graph, 'A')
