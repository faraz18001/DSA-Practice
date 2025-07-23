class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming_edges = {}
        outcoming_edges = {}
        for i in range(1, n + 1):
            incoming_edges[i] = 0
            outcoming_edges[i] = 0

        for edge in trust:
            a, b = edge[0], edge[1]
            outcoming_edges[a] += 1
            incoming_edges[b] += 1

        candidate_judge = -1

        for person_id, count in incoming_edges.items():
            if count == n - 1:
                candidate_judge = person_id
                break
        if candidate_judge == -1:
            return -1


        if outcoming_edges[candidate_judge] == 0:

            return candidate_judge
        else:

            return -1
