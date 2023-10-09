import heapq

def dijkstra(graph, start):
    # Create a dictionary to store the shortest distances from the start node to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Create a priority queue to store nodes with their current distance
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we've already processed this node with a shorter distance
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If this path is shorter than the stored distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph represented as an adjacency dictionary
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

for node, distance in shortest_distances.items():
    print(f"Shortest distance from {start_node} to {node} is {distance}")
