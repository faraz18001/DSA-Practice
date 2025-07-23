# Tree p = [1,2,3]
p = {
    "val": 1,
    "left": {"val": 2, "left": None, "right": None},
    "right": {"val": 3, "left": None, "right": None}
}

# Tree q = [1,2,3]
q = {
    "val": 1,
    "left": {"val": 2, "left": None, "right": None},
    "right": {"val": 3, "left": None, "right": None}
}


def dfs(node):


    stack = [node]
    visited = []

    while len(stack)!=0:
        node = stack.pop()
        if node is not None:
            visited.append(node['val'])



            stack.append(node['right'])

            stack.append(node['left'])
        else:
            stack.append('null')

    return visited


def solution(p,q):
    list_1=dfs(p)
    list_2=dfs(q)

    if list_1==list_2:
        return True
    else:
        return False

res=solution(p,q)
print(res)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node):
            stack = [node]
            visited = []
            while len(stack) != 0:
                node = stack.pop()
                if node is not None:
                    visited.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)
                else:
                    visited.append('null')
            return visited

        list_1 = dfs(p)
        list_2 = dfs(q)
        if list_1 == list_2:
            return True
        else:
            return False
