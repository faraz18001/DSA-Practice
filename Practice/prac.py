def insertion_sort(arr:list):
    for i in range(1,len(arr)-1):
        temp=arr[i]
        j=i-1
        while temp<arr[j] and j>-1:
            arr[j+1]=arr[j]
            arr[j]=temp
            
            j-=1
            
    return arr



            
            
        