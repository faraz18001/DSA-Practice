{{REWRITTEN_CODE}}
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


def dfs(node):

    stack = [node]
    visited = []

    while len(stack) != 0:
        node = stack.pop()
        if node is not None:
            visited.append(node['val'])

            stack.append(node['right'])

            stack.append(node['left'])
        else:
            stack.append('null')

    return visited


def iterativeley_solution(root):
    if root is None:
        return True
    stack = [(root['left'], root['right'])]
    while stack:
        left, right = stack.pop()
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left['val'] != right['val']:
            return False
        stack.append((left['left'], right['right']))
        stack.append((left['right'], right['left']))
    return True


res = iterativeley_solution(root)
print(res)
