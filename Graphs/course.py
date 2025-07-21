numCourses = 2
prerequisites = [[1,0]]
def getNeighbors(G, nodes):
    lst = []
    for i in G[nodes]:
        lst.append(i[0])
    return lst

def canFinish(prerequisites,numCourses):
    adj_list={}


    for i in range(numCourses):

        adj_list[i]=[]


    for crs,prereq in prerequisites:
        adj_list[crs].append(prereq)
    starting_node = 0  # or use S parameter that's passed in

    def dfs(G,S):
        i=0
        visited_list=[]
        stack=[]
        stack.append(starting_node)

        while len(stack)!=0:
            visited=stack.pop()
            neighbours=getNeighbors(G,visited)


            for neigbour in neighbours:
                if neigbour not in visited_list:
                    stack.append(neigbour)
                    break
            visited_list.append(visited)
            i+=1
            # Check for cycle detection
            visited = set()
            rec_stack = set()

            def has_cycle(node):
                if node in rec_stack:
                    return True
                if node in visited:
                    return False

                visited.add(node)
                rec_stack.add(node)

                for neighbor in adj_list[node]:
                    if has_cycle(neighbor):
                        return True

                rec_stack.remove(node)
                return False

            for course in range(numCourses):
                if course not in visited:
                    if has_cycle(course):
                        return False

            return True









































res=canFinish(prerequisites,numCourses)
print(res)
