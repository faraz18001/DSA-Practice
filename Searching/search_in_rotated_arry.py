def search(arr:list):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]>arr[right]:
            left=mid+1
        else:
            right=mid

    min_index=left

    if min_index==0:
        left,right=0,len(arr)-1
        while left<=right:
            if
