
def solution(arr:list):
    def create_bst():
        return {}

    def insert(bst:dict, key):
        if len(bst) == 0:
            bst['root'] = key
            bst['left'] = {}
            bst['right'] = {}
        else:
            if bst['root'] < key:
                insert(bst['right'], key)
            else:
                insert(bst['left'], key)

    bst = create_bst()
    for value in arr:
        insert(bst, value)

    return bst

arr = [-10, -3, 0, 5, 9]

res = solution(arr)
print(res)



