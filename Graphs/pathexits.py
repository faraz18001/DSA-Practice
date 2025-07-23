from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        adj_list = {}

        # Initialize adjacency list
        for i in range(n):
            adj_list[i] = []

        # Build adjacency list from edges
        for edge in edges:
            u, v = edge[0], edge[1]
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(adj_list, starting_node):
            stack = []
            visited = set()
            stack.append(starting_node)
            while len(stack) != 0:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    if node == destination:
                        return True
                    neighbours = adj_list[node]
                    for neighbour in neighbours:
                        if neighbour not in visited:
                            stack.append(neighbour)
            return False

        return dfs(adj_list, source)

res = valid_path(3, [[0,1],[1,2],[2,0]], 0, 2)
print(res)
