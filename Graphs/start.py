edges = [[1,2],[5,1],[1,3],[1,4]]


def solution(edges:list):
    adj_list={}
    for edge in edges:
        u,v=edge[0],edge[1]

        if u not in adj_list:
            adj_list[u]=[]

        if v not in adj_list:
            adj_list[v]=[]

            adj_list[u].append(v)
            adj_list[v].append(u)
    n=len(edges)
    for key,value in adj_list.items():
        if len(value)==n-1:
            return key

res=solution(edges)
print(res)
