def solution(arr:list):
    stack=[]
    for operation in arr:
        if operation=='+':
            stack.append(stack[-1]+stack[-2])
        elif operation=='D':
            stack.append(2*stack[-1])
            
        elif operation=='C':
            stack.pop()
        else:
            stack.append(int(op))