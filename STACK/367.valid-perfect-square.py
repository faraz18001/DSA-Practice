

def solution(x):
    l,r=1,x
    while l<=r:
        mid=(l+r)//2
        if mid*mid==x:
            return True
        elif mid*mid<x:
            l=mid+1
            
        else:
            r=mid-1
            
    return False