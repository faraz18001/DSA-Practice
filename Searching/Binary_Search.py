def binarysearch(arr:list,target:int):
    left,right=0,len(arr)-1
    while left<=right:
        mid_point=(left+right)//2
        if arr[mid_point]==target:
            return mid_point
       
        elif arr[mid_point]<target:
            left=mid_point+1

        else:
            right=mid_point-1

    return -1



test_arr = [1, 3, 5, 7, 8]
res=binarysearch(test_arr,9)
print(res)

    
        

    
