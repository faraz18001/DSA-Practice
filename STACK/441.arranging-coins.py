def arrange(x):
    left,right=1,x
    res=0
    while left<=right:
        mid=(left+right)//2
        coins=(mid*(mid+1))//2
        
        if coins<x:
            res=mid
            left=mid+1
            
        else:
            right=mid-1
            
    return res

            
            
        
        