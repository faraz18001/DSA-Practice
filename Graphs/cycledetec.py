# Test cases for your has_cycle function

def getNeighbors(G, node):
    """Helper function - replace with your actual implementation"""
    if node < len(G):
        return G[node]
    return []

def has_cycle(G, s):
    stack = [s]
    visited = []
    rec_stack = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            rec_stack.append(node)
            stack.append(node)

            neighbours = getNeighbors(G, node)
            for neighbour in neighbours:
                if neighbour not in visited:
                    stack.append(neighbour)
                else:
                    if neighbour in rec_stack:
                        return True
        else:
            if node in rec_stack:
                rec_stack.remove(node)

    return False

# Test Case 1: Simple cycle (0 -> 1 -> 2 -> 0)
G1 = [
    [1],    # Node 0 points to 1
    [2],    # Node 1 points to 2
    [0]     # Node 2 points to 0 (creates cycle)
]

# Test Case 2: No cycle (tree structure)
G2 = [
    [1, 2], # Node 0 points to 1 and 2
    [3],    # Node 1 points to 3
    [4],    # Node 2 points to 4
    [],     # Node 3 has no neighbors
    []      # Node 4 has no neighbors
]

# Test Case 3: Self loop
G3 = [
    [0],    # Node 0 points to itself
    [2],    # Node 1 points to 2
    []      # Node 2 has no neighbors
]

# Test Case 4: Larger cycle
G4 = [
    [1],    # 0 -> 1
    [2],    # 1 -> 2
    [3],    # 2 -> 3
    [4],    # 3 -> 4
    [1]     # 4 -> 1 (creates cycle)
]

# Test Case 5: No cycle - disconnected
G5 = [
    [1],    # 0 -> 1
    [],     # 1 has no neighbors
    [3],    # 2 -> 3
    []      # 3 has no neighbors
]

# Run tests
print("TEST RESULTS:")
print(f"G1 (simple cycle): {has_cycle(G1, 0)} - Should be True")
print(f"G2 (no cycle tree): {has_cycle(G2, 0)} - Should be False")
print(f"G3 (self loop): {has_cycle(G3, 0)} - Should be True")
print(f"G4 (larger cycle): {has_cycle(G4, 0)} - Should be True")
print(f"G5 (no cycle): {has_cycle(G5, 0)} - Should be False")

# Test different starting points
print(f"\nG4 starting from node 2: {has_cycle(G4, 2)} - Should be True")
print(f"G5 starting from node 2: {has_cycle(G5, 2)} - Should be False")
