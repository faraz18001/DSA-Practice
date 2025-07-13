class Solution:
    def isValid(self, s: str) -> bool:
        mapping = { ")":"(", "}":"{", "]":"[" }
        stack=[]  
        for char in s:
            if char in mapping.values():
                stack.append(char)
            if char in mapping.keys():
                if len(stack)!=0:
                    popped=stack.pop()
                    if popped!=mapping[char]:
                        return False
                else:
                    return False
        
       
        return len(stack) == 0