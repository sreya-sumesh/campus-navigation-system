import heapq

# 1. Map of USAR Campus (Distances in meters)
usar_campus = {
    # --- GROUND FLOOR (Fully Interconnected) ---
    
    'Gate 1': [('Gate 2', 1000), ('Block A', 100), ('Admin Block (Ground)', 100), 
               ('Block B', 100), ('Auditorium', 800)],
               
    'Gate 2': [('Gate 1', 1000), ('Block A', 1000), ('Admin Block (Ground)', 1000), 
               ('Block B', 1000), ('Auditorium', 200)],
    
    'Block A': [('Gate 1', 100), ('Gate 2', 1000), ('Admin Block (Ground)', 20), 
                ('Block B', 40), ('Auditorium', 800), ('Canteen (Basement)', 50)],
                
    'Admin Block (Ground)': [('Gate 1', 100), ('Gate 2', 1000), ('Block A', 20), 
                             ('Block B', 20), ('Auditorium', 800), ('Library (5th Floor)', 20)],
                             
    'Block B': [('Gate 1', 100), ('Gate 2', 1000), ('Block A', 40), 
                ('Admin Block (Ground)', 20), ('Auditorium', 800), ('Canteen (Basement)', 10)],
    
    'Auditorium': [('Gate 1', 800), ('Gate 2', 200), ('Block A', 800), 
                   ('Admin Block (Ground)', 800), ('Block B', 800)],
    
    # --- OTHER FLOORS (Only accessible from specific ground locations) ---
    
    # 5th Floor
    'Library (5th Floor)': [('Admin Block (Ground)', 20)],
    
    # Basement
    'Canteen (Basement)': [('Block B', 10), ('Block A', 50)]
}

# 2. Dijkstra's Algorithm
def find_shortest_path(graph, start, destination):
    # Check if inputs are valid
    if start not in graph or destination not in graph:
        return None, []
        
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start, [start])] # (current_cost, current_node, path_taken)

    while pq:
        current_dist, current_node, path = heapq.heappop(pq)

        # If we reached the destination, return the result
        if current_node == destination:
            return current_dist, path

        # Skip if we found a shorter path already
        if current_dist > distances[current_node]:
            continue

        # Check all connected neighboring locations
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            # If this new path is shorter, update it and add to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor, path + [neighbor]))

    return float('inf'), []

# 3. Interactive User Input

aliases = {
    "gate 1": "Gate 1",
    "gate 2": "Gate 2",
    "block a": "Block A",
    "block b": "Block B",
    "admin block": "Admin Block (Ground)",
    "admin": "Admin Block (Ground)",
    "library": "Library (5th Floor)",
    "canteen": "Canteen (Basement)",
    "auditorium": "Auditorium",
    "audi": "Auditorium"
}

# Clean list for display
display_locations = [
    "Gate 1", "Gate 2", "Block A", "Admin Block", 
    "Block B", "Library", "Canteen", "Auditorium"
]

print("--- USAR Campus Navigation System ---")
print("Available Locations:")
for loc in display_locations:
    print(f"- {loc}")
print("-" * 37)

# Take input and convert it to lowercase
raw_start = input("Enter starting location: ").strip().lower()
raw_end = input("Enter destination: ").strip().lower()

# Map the simple input to the exact graph key
start_node = aliases.get(raw_start, raw_start)
end_node = aliases.get(raw_end, raw_end)

cost, path = find_shortest_path(usar_campus, start_node, end_node)

# Output results
print("\n--- Route Details ---")
if cost is None:
    print("Error: Invalid location entered. Please check spelling and try again.")
elif cost == float('inf'):
    print("No route found between these locations.")
else:
    print(f"Shortest Distance: {cost} meters")
    print(f"Optimal Route: {' -> '.join(path)}")
