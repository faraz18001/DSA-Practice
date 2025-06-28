def binarysearch(arr:list,target:int):
    left,right=0,len(arr)-1
    mid_point=len(arr)//2

    if arr[mid_point]==target:
        return [mid_point]
    
    while left<=right:
        if arr[mid_point]<target:
            left=mid_point
        if arr[mid_point]>target:
            right=mid_point
        

    
