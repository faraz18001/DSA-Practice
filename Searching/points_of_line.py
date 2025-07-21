import math
def length_of_line_your_way(points_lists, target_length):
    """
    EXACT same logic as your original solution!
    Treating each length as a "row" in our sorted array.
    """
    
    def calculate_distance(line):
        x1, y1, x2, y2 = line
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Create array of lengths (our "arr")
    arr = []
    for line in points_lists:
        length = calculate_distance(line)
        arr.append(length)
    
    # Sort the array - now arr[0] has smallest length, arr[-1] has largest
    arr.sort()
    
    # YOUR EXACT LOGIC - just replace target with target_length:
    top, bottom = 0, len(arr) - 1
    epsilon = 1e-9
    
    while top <= bottom:
        current_row = (top + bottom) // 2
        
        # In your original: if arr[current_row][0] < target
        # Here: if arr[current_row] < target_length (since each "row" has one value)
        if arr[current_row] < target_length - epsilon:
            top = current_row + 1
            
        # In your original: if arr[current_row][-1] > target  
        # Here: if arr[current_row] > target_length (since each "row" has one value)
        elif arr[current_row] > target_length + epsilon:
            bottom = current_row - 1
            
        else:
            # Found the range! Now search within this "row"
            break
    else:
        return False
    
    # Stage 2: Search within the "row" (in our case, just check if we found exact match)
    # Since each "row" has only one element, we can directly check
    if abs(arr[current_row] - target_length) < epsilon:
        return True
    
    return False


points1 = [[0, 0, 3, 4], [1, 1, 4, 5], [0, 0, 1, 1]]
target1 = 10.0
res=length_of_line_your_way(points1,target1)
print(res)
