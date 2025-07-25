
from typing_extensions import NoDefault


root = {
    "val": 1,
    "left": {
        "val": 2,
        "left": {"val": 3, "left": None, "right": None},
        "right": {"val": 4, "left": None, "right": None}
    },
    "right": {
        "val": 2,
        "left": {"val": 4, "left": None, "right": None},
        "right": {"val": 3, "left": None, "right": None}
    }
}

"""def dfs(root):
    stack=[root]
    visited=set()
    while len(stack)!=0:
        node=stack.pop()
        if node not in visited:
            visited.add(node['val'])

            stack.append(node['left']
            )

            stack.append(node['right']


            )
    return visited
res=dfs(root)
print(res)
"""


def solution(root):
    def dfs(left, right):
        if root['left'] is None and root['right'] is None:
            return True  # Single node is symmetric by the definition

        if left['left'] is None or right['left'] is None:
            return True

        if left['left'] == right['left'] and left['right'] == right['left']:
            return True
        return False
    return dfs(root['left'], root['right'])

res=solution(root)
print(res)
