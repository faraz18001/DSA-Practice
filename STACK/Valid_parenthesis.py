def valid(s:str):
    stack=[]
    for char in s:
        if char=='(':
            stack.append(char)
        if char==")":
            if len(stack)!=0:
                stack.pop()
            else:
                return False

    if len(stack)==0:
        return True
    return False