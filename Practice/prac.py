def sqrt(x):
    res=0
    left,right=0,x
    while left<=right:
        mid=(left+right)//2
        
        if mid**2==x:
            return mid
        
        if mid**2<x:
            res=mid
            left=mid+1
            
        else:
            right=mid-1
            
    return res