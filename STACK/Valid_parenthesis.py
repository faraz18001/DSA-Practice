def valid(s:str):
    stack=[]
    for char in s:
        if char=='(':
            stack.append(char)
        if char==")":
            stack.pop()

    if len(stack)==0:
        return True
    return False

