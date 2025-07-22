def has_cycle(G, s):
    stack = [s]
    visited = [False] * len(G)
    rec_stack = [False] * len(G)

    while stack:
        node = stack.pop()

        if visited[node] == False:
            visited[node] = True
            rec_stack[node] = True
            stack.append(node)

            neighbours = getNeighbors(G, node)
            for neighbour in neighbours:
                if visited[neighbour] == False:
                    stack.append(neighbour)
                else:
                    if rec_stack[neighbour]:
                        return True
        else:
            rec_stack[node] = False

    return False
