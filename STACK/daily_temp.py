class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]
        
        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
    


def solution(temp:list):
    res=[0]*len(temp)
    stack=[]
    for i in range(len(temp)):
        t=temp[i]
        while len(stack) is not None and t>stack[-1][0]:
            stack_T,stack_i=stack.pop()
            res[stack_i]=i-stack_i
        stack.append((t,i))
    return res