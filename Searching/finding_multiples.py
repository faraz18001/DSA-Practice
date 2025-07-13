def binary_search(arr: list, target: int):
    """
    Standard binary search implementation.
    Returns the index of target if found, -1 otherwise.
    Assumes arr is sorted in ascending order.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid_point = (left + right) // 2
        
        if arr[mid_point] == target:
            return mid_point  
        elif arr[mid_point] < target:
            left = mid_point + 1
        else:
            right = mid_point - 1
    
    return -1 

def find_multiples_after_target(arr: list, target: int):
   
    target_index = binary_search(arr, target)
    
    if target_index == -1:
        return [] 
    
    result = []
   
    for i in range(target_index, len(arr)):
        if arr[i] % target == 0:
            result.append(i)
    
    return result


# Example usage:
if __name__ == "__main__":
    # Test the corrected binary search
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    result = binary_search(sorted_array, target)
    print(f"Binary search for {target}: index {result}")
    
    # Test the multiples function
    array_with_multiples = [2, 4, 6, 8, 10, 12, 14, 16]
    target = 4
    multiples = find_multiples_after_target(array_with_multiples, target)
    print(f"Indices of multiples of {target}: {multiples}")