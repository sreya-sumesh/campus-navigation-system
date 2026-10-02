# Architectural Decisions & Graph Logic

## Algorithm Selection
- Selected **Dijkstra's Algorithm** over Breadth-First Search (BFS) because the campus pathways represent a **weighted graph** (varying distances and staircases).
- Utilized Python's `heapq` module (Min-Heap implementation) to maintain $O((V + E) \log V)$ time complexity.

## Graph Connectivity & Bypassing Structural Constraints
- **Initial Logic:** Ground-level navigation between buildings was initially constrained through central nodes (e.g., routing through Admin Block).
- **Refined Decision:** Updated graph edges to connect all ground-level nodes (`Block A`, `Block B`, `Admin Block`, `Auditorium`, `Gate 1`, `Gate 2`) directly. This aligns with physical campus layout where outdoor walkways bypass building interiors.
- **Vertical Navigation:** Floor movements (Library on 5th floor, Canteen in Basement) remain strictly routed through designated access points (`Admin Block` for Library, `Block B`/`Block A` for Canteen).
