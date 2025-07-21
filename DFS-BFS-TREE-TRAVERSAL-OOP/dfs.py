def bfs(self):
    current_node=self.root
    queue=[]
    result=[]

    queue.append(current_node)

    while len(queue)>0:
        current_node=queue.pop(0)
        result.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    return result


dfs_post_order(self):
    result=[]
