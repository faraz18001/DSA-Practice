def binary_rec(arr,target,left=0,right=None):
    if right is None:
        right=len(arr)-1
    
    if left>right:
        return -1
    
    mid=(left+right)//2
    
    if arr[mid]==target:
        return mid
    
    if arr[mid]<target:
        return binary_rec(arr,target,mid+1,right)
    else:
        return binary_rec(arr,target,left,mid-1)


