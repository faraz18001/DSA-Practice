def binary_search(arr:list,target:int):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        if arr[left]<target:
            left=mid+1

        elif arr[right]>target:
            right=mid-1

    return -1
