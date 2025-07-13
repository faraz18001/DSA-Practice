def get_min_stack(value):
    stack = []
    min_stack = []
    
    stack.append(value)
    min_stack.append(value)  
    
    min_value = min(stack.pop(), min_stack.pop())
    min_stack.append(min_value)
    
    return min_stack.pop()

