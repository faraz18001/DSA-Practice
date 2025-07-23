class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj_list = {}
        for edge in edges:
            u, v = edge[0], edge[1]

            if u not in adj_list:
                adj_list[u] = []

            if v not in adj_list:
                adj_list[v] = []

            adj_list[u].append(v)
            adj_list[v].append(u)

        n = len(edges) + 1
        for key, value in adj_list.items():
            if len(value) == n - 1:
                return key
