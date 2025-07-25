import re
from helper import*

root = {
    "val": 3,
    "left": {
        "val": 9,
        "left": None,
        "right": None
    },
    "right": {
        "val": 20,
        "left": {
            "val": 15,
            "left": None,
            "right": None
        },
        "right": {
            "val": 7,
            "left": None,
            "right": None
        }
    }
}



def bfs(root):
    queue = [root]
    visited = []
    level_average = []

    while queue:
        level_size = len(queue)
        res = []

        for i in range(level_size):
            node = queue.pop(0)
            visited.append(node)
            res.append(node['val'])
            if node['left'] is not None:
                queue.append(node['left'])
            if node['right'] is not None:
                queue.append(node['right'])

        level_average.append(sum(res) // len(res))

    return level_average

res = bfs(root)
print(res)
