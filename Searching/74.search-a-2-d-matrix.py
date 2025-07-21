def solution(arr:list,target:int):
    top,bottom=0,len(arr)-1
    while top<=bottom:
        current_row=(top+bottom)//2
        
        if arr[current_row][0]<target:
            bottom=current_row-1
            
        if arr[current_row][-1]>target:
            top=current_row+1
            
        else:
            break
        
    else:
        return False
    
    
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[current_row][mid]<target:
            left=mid+1
        
        elif arr[current_row][mid]>target:
            right=mid-1
            
        else:
            return True
        
    return False
        
    
    
    
    
    



