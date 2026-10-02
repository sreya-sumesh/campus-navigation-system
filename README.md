# USAR Campus Navigation System

A DSA-based campus navigation system designed for the USAR (GGSIPU East Delhi Campus) layout. Built in pure Python using **Dijkstra's Algorithm** to find the shortest walking paths between key campus locations.

## Features
- **Graph Representation:** Models campus locations as nodes and physical walking distances (in meters) as edge weights.
- **Multi-Level Navigation:** Supports vertical movement (Library on the 5th floor) and basement access (Canteen) alongside outdoor ground-level paths.
- **User-Friendly Input:** Includes case-insensitive alias mapping so users can type simple names like `library` or `canteen`.
- **Automated Test Suite:** Built-in validation script to verify connectivity across all campus nodes.

## Campus Locations Included
- **Gates:** Gate 1, Gate 2
- **Main Building:** Block A (USAR), Admin Block (Ground), Block B (USDI)
- **Special Locations:** Library (5th Floor), Canteen (Basement), Auditorium
